from apiarmor.shared import DotDict, hash_message, get_timestamp_utc


class ApiArmorClient:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def sign(self, url, body):
        timestamp = get_timestamp_utc()
        _hash = hash_message(self.secret_key, timestamp, url, body)
        output = {"timestamp": timestamp, "hash": _hash}
        return DotDict(output)
