from ..shared import hash_message, get_timestamp_utc


class ApiArmorClient:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def signature(self, url, query, body):
        timestamp = get_timestamp_utc()
        return hash_message(self.secret_key, timestamp, url, query, body)
