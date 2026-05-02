from typing import TYPE_CHECKING
from . import _rust
from ._rust import (
    __version__,
    PrivateKey,
    PublicKey,
    SessionKeys,
    crypto_auth,
    crypto_auth_verify,
    crypto_box_beforenm,
    generate_rsa_prime,
    generate_safe_prime,
    generate_session_keys,
    is_prime,
    EndpointNotOpenError,
    InvalidAddressError,
)

if TYPE_CHECKING:
    from .endpoint import Endpoint


def __getattr__(name: str):
    if name == "Endpoint":
        from .endpoint import Endpoint
        return Endpoint
    if hasattr(_rust, name):
        return getattr(_rust, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "__version__",
    "Endpoint",
    "PrivateKey",
    "PublicKey",
    "SessionKeys",
    "crypto_auth",
    "crypto_auth_verify",
    "crypto_box_beforenm",
    "generate_rsa_prime",
    "generate_safe_prime",
    "generate_session_keys",
    "is_prime",
    "EndpointNotOpenError",
    "InvalidAddressError",
]
