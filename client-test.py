from apiarmor.client.apiarmor_client import ApiArmorClient

# Your secret key (keep this secret)
secret_key = "12345678"  # do not hard code this! use secret or env variable
api_armor_client = ApiArmorClient(secret_key)


# Your data to send
data_to_send = {"key1": "value1", "key2": "value2"}


url = "http://127.0.0.1:5000"

signed_request = api_armor_client.sign(url, body=data_to_send)

# Get the hash and timestamp from the signed request
hash_to_send = signed_request.hash
timestamp_to_send = signed_request.timestamp

# Now, send the request to the server with the hash and timestamp in the headers
headers = {"Hash": hash_to_send, "Timestamp": str(timestamp_to_send)}
response = api_armor_client.send_request(url, body=data_to_send, headers=headers)

# Process the server response as needed
print(response.text)

# Print the server res
