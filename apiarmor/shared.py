import json
from hashlib import sha256
from datetime import datetime, timezone


class DotDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def get_timestamp_utc():
    current_utc_time = datetime.now(timezone.utc)
    utc_timestamp = int(current_utc_time.timestamp())
    return utc_timestamp


def hash_message(secret_key, timestamp, url, body):
    delimiter = "-"
    message = ""
    message += url + delimiter
    message += json.dumps(body) + delimiter
    message += str(timestamp) + delimiter
    message += secret_key
    hash = sha256(message.encode("utf-8")).hexdigest()
    return hash
