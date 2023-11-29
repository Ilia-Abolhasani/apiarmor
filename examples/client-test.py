from apiarmor.client.utils import send_data_to_server, hash_message

# Your data to send
data_to_send = {"key1": "value1", "key2": "value2"}

# Your secret key (keep this secret)
secret_key = b"your_secret_key"

# Hash the message on the client side
hashed_key, hashed_data = hash_message(str(data_to_send), secret_key)

# The URL of your server
server_url = "http://127.0.0.1:5000"  # Update with your server URL

# Send the data to the server
response = send_data_to_server(hashed_data, hashed_key, server_url)

# Print the server res
