from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def hash_message(message, secret_key):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=b"salt",
        iterations=100000,
        length=32,
        backend=default_backend(),
    )
    key = kdf.derive(secret_key)
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(message)
    return key, digest.finalize()
