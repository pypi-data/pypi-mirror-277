"""
Server for Commune modules.
"""

import json
import random
import re
import sys
from datetime import datetime, timezone
from functools import partial
from time import sleep
from typing import Any, Awaitable, Callable, ParamSpec, TypeVar

import fastapi
import starlette.datastructures
from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from pydantic import BaseModel
from scalecodec.utils.ss58 import ss58_encode  # type: ignore
from substrateinterface import Keypair  # type: ignore

from communex._common import get_node_url
from communex.client import CommuneClient
from communex.key import check_ss58_address
from communex.module import _signer as signer
from communex.module._rate_limiters.limiters import (IpLimiterMiddleware,
                                                     IpLimiterParams,
                                                     StakeLimiterMiddleware,
                                                     StakeLimiterParams)
from communex.module._util import log
from communex.module.module import EndpointDefinition, Module, endpoint
from communex.types import Ss58Address
from communex.util.memo import TTLDict

# Regular expression to match a hexadecimal number
HEX_PATTERN = re.compile(r"^[0-9a-fA-F]+$")

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")

P = ParamSpec("P")
R = TypeVar("R")


def retry(max_retries: int | None, retry_exceptions: list[type]):
    assert max_retries is None or max_retries > 0

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            max_retries__ = max_retries or sys.maxsize  # TODO: fix this ugly thing
            for tries in range(max_retries__ + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if any(isinstance(e, exception_t) for exception_t in retry_exceptions):
                        func_name = func.__name__
                        log(f"An exception occurred in '{func_name} on try {tries}': {e}, but we'll retry.")
                        if tries < max_retries__:
                            delay = (1.4 ** tries) + random.uniform(0, 1)
                            sleep(delay)
                            continue
                    raise e
            raise Exception("Unreachable")
        return wrapper
    return decorator


# TODO: merge `is_hex_string` into `parse_hex`
def is_hex_string(string: str):
    return bool(HEX_PATTERN.match(string))


def parse_hex(hex_str: str) -> bytes:
    if hex_str[0:2] == "0x":
        return bytes.fromhex(hex_str[2:])
    else:
        return bytes.fromhex(hex_str)


def build_input_handler_route_class(
    subnets_whitelist: list[int] | None,
    module_key: Ss58Address,
    request_staleness: int,
    blockchain_cache: TTLDict[str, list[Ss58Address]],
    host_key: Keypair,
    use_testnet: bool,
) -> type[APIRoute]:
    class InputHandlerRoute(APIRoute):
        def get_route_handler(self):
            original_route_handler = super().get_route_handler()

            async def custom_route_handler(request: Request) -> Response:
                body = await request.body()

                # TODO: we'll replace this by a Result ADT :)
                match self._check_inputs(request, body, module_key):
                    case (False, error):
                        return error
                    case (True, _):
                        pass

                body_dict: dict[str, dict[str, Any]] = json.loads(body)
                timestamp = body_dict['params'].get("timestamp", None)
                legacy_timestamp = request.headers.get("X-Timestamp", None)
                try:
                    timestamp_to_use = timestamp if not legacy_timestamp else legacy_timestamp
                    request_time = datetime.fromisoformat(timestamp_to_use)
                except Exception:
                    return JSONResponse(status_code=400, content={"error": "Invalid ISO timestamp given"})
                if (datetime.now(timezone.utc) - request_time).total_seconds() > request_staleness:
                    return JSONResponse(status_code=400, content={"error": "Request is too stale"})
                response: Response = await original_route_handler(request)
                return response

            return custom_route_handler

        @staticmethod
        def _check_inputs(request: Request, body: bytes, module_key: Ss58Address):
            required_headers = ["x-signature", "x-key", "x-crypto"]
            optional_headers = ["x-timestamp"]

            # TODO: we'll replace this by a Result ADT :)
            match _get_headers_dict(request.headers, required_headers, optional_headers):
                case (False, error):
                    return (False, error)
                case (True, headers_dict):
                    pass

            # TODO: we'll replace this by a Result ADT :)
            match _check_signature(headers_dict, body, module_key):
                case (False, error):
                    return (False, error)
                case (True, _):
                    pass

            # TODO: we'll replace this by a Result ADT :)
            match _check_key_registered(
                subnets_whitelist,
                headers_dict,
                blockchain_cache,
                host_key,
                use_testnet,
            ):
                case (False, error):
                    return (False, error)
                case (True, _):
                    pass

            return (True, None)

    return InputHandlerRoute


def _json_error(code: int, message: str):
    return JSONResponse(status_code=code, content={"error": {"code": code, "message": message}})


def _get_headers_dict(
    headers: starlette.datastructures.Headers,
    required: list[str],
    optional: list[str],
):
    headers_dict: dict[str, str] = {}
    for required_header in required:
        value = headers.get(required_header)
        if not value:
            code = 400
            return False, _json_error(code, f"Missing header: {required_header}")
        headers_dict[required_header] = value
    for optional_header in optional:
        value = headers.get(optional_header)
        if value:
            headers_dict[optional_header] = value

    return True, headers_dict


# TODO: type `headers_dict` better
def _check_signature(
    headers_dict: dict[str, str],
    body: bytes,
    module_key: Ss58Address
):
    key = headers_dict["x-key"]
    signature = headers_dict["x-signature"]
    crypto = int(headers_dict["x-crypto"])  # TODO: better handling of this

    if not is_hex_string(key):
        return (False, _json_error(400, "X-Key should be a hex value"))

    signature = parse_hex(signature)
    key = parse_hex(key)

    timestamp = headers_dict.get("x-timestamp")
    legacy_verified = False
    if timestamp:
        # tries to do a legacy verification
        json_body = json.loads(body)
        json_body["timestamp"] = timestamp
        stamped_body = json.dumps(json_body).encode()
        legacy_verified = signer.verify(key, crypto, stamped_body, signature)

    verified = signer.verify(key, crypto, body, signature)
    if not verified and not legacy_verified:
        return (False, _json_error(401, "Signatures doesn't match"))

    body_dict: dict[str, dict[str, Any]] = json.loads(body)
    target_key = body_dict['params'].get("target_key", None)
    if not target_key or target_key != module_key:
        return (False, _json_error(401, "Wrong target_key in body"))

    return (True, None)


@retry(5, [Exception])
def _make_client(node_url: str):
    return CommuneClient(url=node_url, num_connections=1, wait_for_finalization=False)


def _check_key_registered(
        subnets_whitelist: list[int] | None,
        headers_dict: dict[str, str],
        blockchain_cache: TTLDict[str, list[Ss58Address]],
        host_key: Keypair,
        use_testnet: bool,
):
    key = headers_dict["x-key"]
    if not is_hex_string(key):
        return (False, _json_error(400, "X-Key should be a hex value"))
    key = parse_hex(key)

    # TODO: checking for key being registered should be smarter
    # e.g. query and store all registered modules periodically.

    ss58_format = 42
    ss58 = ss58_encode(key, ss58_format)
    ss58 = check_ss58_address(ss58, ss58_format)

    # If subnets whitelist is specified, checks if key is registered in one
    # of the given subnets

    allowed_subnets: dict[int, bool] = {}
    caller_subnets: list[int] = []
    if subnets_whitelist is not None:
        def query_keys(subnet: int):
            try:
                node_url = get_node_url(None, use_testnet=use_testnet)
                client = _make_client(node_url)  # TODO: get client from outer context
                return [*client.query_map_key(subnet).values()]
            except Exception:
                log(
                    "WARNING: Could not connect to a blockchain node"
                )
                return_list: list[Ss58Address] = []
                return return_list

        # TODO: client pool for entire module server

        got_keys = False
        no_keys_reason = (
            "Miner could not connect to a blockchain node "
            "or there is no key registered on the subnet(s) {} "
        )
        for subnet in subnets_whitelist:
            get_keys_on_subnet = partial(query_keys, subnet)
            cache_key = f"keys_on_subnet_{subnet}"
            keys_on_subnet = blockchain_cache.get_or_insert_lazy(
                cache_key, get_keys_on_subnet
            )
            if len(keys_on_subnet) == 0:
                reason = no_keys_reason.format(subnet)
                log(f"WARNING: {reason}")
            else:
                got_keys = True

            if host_key.ss58_address not in keys_on_subnet:
                log(
                    f"WARNING: This miner is deregistered on subnet {subnet}"
                )
            else:
                allowed_subnets[subnet] = True
            if ss58 in keys_on_subnet:
                caller_subnets.append(subnet)
        if not got_keys:
            return False, _json_error(503, no_keys_reason.format(subnets_whitelist))
        if not allowed_subnets:
            log("WARNING: Miner is not registered on any subnet")
            return False, _json_error(403, "Miner is not registered on any subnet")

        # searches for a common subnet between caller and miner
        # TODO: use sets
        allowed_subnets = {
            subnet: allowed for subnet, allowed in allowed_subnets.items() if (
                subnet in caller_subnets
            )
        }
        if not allowed_subnets:
            return False, _json_error(
                403, "Caller key is not registered in any subnet that the miner is"
            )
    else:
        # accepts everything
        pass

    return (True, None)


Callback = Callable[[Request], Awaitable[Response]]


class ModuleServer:
    def __init__(
        self,
        module: Module,
        key: Keypair,
        max_request_staleness: int = 120,
        whitelist: list[str] | None = None,
        blacklist: list[str] | None = None,
        subnets_whitelist: list[int] | None = None,
        lower_ttl: int = 600,
        upper_ttl: int = 700,
        limiter: StakeLimiterParams | IpLimiterParams = StakeLimiterParams(),
        ip_blacklist: list[str] | None = None,
        use_testnet: bool = False,
    ) -> None:
        self._module = module
        self._app = fastapi.FastAPI()
        self._subnets_whitelist = subnets_whitelist
        self.key = key
        self.max_request_staleness = max_request_staleness
        self._blacklist = blacklist
        self._whitelist = whitelist
        ttl = random.randint(lower_ttl, upper_ttl)
        self._blockchain_cache = TTLDict[str, list[Ss58Address]](ttl)
        self._ip_blacklist = ip_blacklist

        # Midlewares

        if isinstance(limiter, StakeLimiterParams):
            self._app.add_middleware(
                StakeLimiterMiddleware,
                subnets_whitelist=self._subnets_whitelist,
                params=limiter,
            )
        else:
            self._app.add_middleware(
                IpLimiterMiddleware, params=limiter
            )

        self.register_extra_middleware()

        # Routes
        self._router = APIRouter(
            route_class=build_input_handler_route_class(
                self._subnets_whitelist,
                check_ss58_address(self.key.ss58_address),
                self.max_request_staleness,
                self._blockchain_cache,
                self.key,
                use_testnet
            )
        )
        self.register_endpoints(self._router)
        self._app.include_router(self._router)

    def get_fastapi_app(self):
        return self._app

    def register_endpoints(self, router: APIRouter):
        endpoints = self._module.get_endpoints()
        for name, endpoint_def in endpoints.items():

            class Body(BaseModel):
                params: endpoint_def.params_model  # type: ignore

            def handler(end_def: EndpointDefinition[Any, ...], body: Body):

                return end_def.fn(self._module, **body.params.model_dump())  # type: ignore

            defined_handler = partial(handler, endpoint_def)
            router.post(f"/method/{name}")(defined_handler)

    def register_extra_middleware(self):
        async def check_lists(request: Request, call_next: Callback):

            if not request.url.path.startswith('/method'):
                return await call_next(request)
            key = request.headers.get("x-key")
            if not key:
                return _json_error(400, "Missing header: X-Key")
            ss58_format = 42
            ss58 = ss58_encode(key, ss58_format)
            ss58 = check_ss58_address(ss58, ss58_format)

            if request.client is None:
                return _json_error(400, "Address should be present in request")
            if self._blacklist and ss58 in self._blacklist:
                return _json_error(403, "You are blacklisted")
            if self._ip_blacklist and request.client.host in self._ip_blacklist:
                return _json_error(403, "Your IP is blacklisted")
            if self._whitelist and ss58 not in self._whitelist:
                return _json_error(403, "You are not whitelisted")
            response = await call_next(request)
            return response

        self._app.middleware("http")(check_lists)

    def add_to_blacklist(self, ss58_address: str | Ss58Address):
        if not self._blacklist:
            self._blacklist = []
        self._blacklist.append(ss58_address)

    def add_to_whitelist(self, ss58_address: str | Ss58Address):
        if not self._whitelist:
            self._whitelist = []
        self._whitelist.append(ss58_address)


def main():
    class Amod(Module):
        @endpoint
        def do_the_thing(self, awesomness: int = 42):
            if awesomness > 60:
                msg = f"You're super awesome: {awesomness} awesomness"
            else:
                msg = f"You're not that awesome: {awesomness} awesomness"
            return {"msg": msg}

    a_mod = Amod()
    keypair = Keypair.create_from_mnemonic(signer.TESTING_MNEMONIC)
    server = ModuleServer(a_mod, keypair, subnets_whitelist=None)
    app = server.get_fastapi_app()

    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)  # type: ignore


if __name__ == "__main__":
    main()
