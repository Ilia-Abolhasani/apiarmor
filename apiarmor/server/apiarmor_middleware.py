import time
from flask import abort, request
from ..shared import hash_message, get_timestamp_utc


class ApiArmorMiddleware:
    def __init__(
        self,
        secret_key,
        ip_whitelist=None,
        min_time_difference=60,
    ):
        self.secret_key = secret_key
        self.ip_whitelist = set(ip_whitelist) if ip_whitelist else None
        self.min_time_difference = min_time_difference

    def _get_client_timestamp(self):
        client_timestamp = request.headers.get("Timestamp")

        if not client_timestamp:
            abort(400, "Timestamp is missing in the request.")

        try:
            client_timestamp = float(client_timestamp)
        except ValueError:
            abort(400, "Invalid timestamp format.")
        return client_timestamp

    def _validate_ip(self):
        if self.ip_whitelist is not None:
            client_ip = request.remote_addr
            if client_ip not in self.ip_whitelist:
                abort(401, f"Unauthorized: IP address {client_ip} not in whitelist.")

    def _validate_route(self):
        pass

    def _validate_timestamp(self, client_timestamp):
        current_timestamp = get_timestamp_utc()
        time_difference = abs(current_timestamp - client_timestamp)

        if time_difference > self.min_time_difference:
            abort(401, "Unauthorized: Request timestamp is too old or in the future.")

    def _validate_signature(self, client_timestamp):
        body = request.data
        client_hash = request.headers.get("Hash")

        if not client_hash:
            abort(400, "Hash is missing in the request.")

        # hash body and timestamp
        hashed_message = hash_message()
        if client_hash != hashed_message:
            abort(401, "Unauthorized: Hash mismatch.")

    def __call__(self):
        # ip validation
        self._validate_ip()

        # route validation
        self._validate_route()

        # clinet time
        client_timestamp = self._get_client_timestamp()

        # timestamp validation
        self._validate_timestamp(client_timestamp)

        # hash signature validation
        self._validate_signature(client_timestamp)
