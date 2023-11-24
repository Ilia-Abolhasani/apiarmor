import time
from flask import abort, request
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class APIArmorMiddleware:
    def __init__(self, secret_key, min_time_difference=60, ip_whitelist=None):
        self.secret_key = secret_key
        self.min_time_difference = min_time_difference
        self.ip_whitelist = set(ip_whitelist) if ip_whitelist else None
        
    def _get_client_timestamp(self):
        client_timestamp = request.headers.get('Timestamp')

        if not client_timestamp:
            abort(400, 'Timestamp is missing in the request.')

        try:
            client_timestamp = float(client_timestamp)
        except ValueError:
            abort(400, 'Invalid timestamp format.')
        return client_timestamp
    
    def _validate_timestamp(self, client_timestamp):
        current_timestamp = time.time()

    def hash_message(self, message):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            salt=b'salt',
            iterations=100000,
            length=32,
            backend=default_backend()
        )
        key = kdf.derive(self.secret_key)
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(message)
        return key, digest.finalize()

    def validate_ip(self):
        if self.ip_whitelist is not None:
            client_ip = request.remote_addr
            if client_ip not in self.ip_whitelist:
                abort(401, f'Unauthorized: IP address {client_ip} not in whitelist.')

    def __call__(self):
        self.validate_ip()
                
        

        time_difference = abs(server_timestamp - client_timestamp)

        if time_difference > self.min_time_difference:
            abort(401, 'Unauthorized: Request timestamp is too old or in the future.')

        message_body = request.data
        client_hash = request.headers.get('Hash')

        if not client_hash:
            abort(400, 'Hash is missing in the request.')

        key, hashed_message = self.hash_message(message_body)

        if client_hash != hashed_message:
            abort(401, 'Unauthorized: Hash mismatch.')
