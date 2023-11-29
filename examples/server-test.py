from flask import Flask, jsonify
from apiarmor.server.middleware import APIArmorMiddleware

app = Flask(__name__)

# Instantiate APIArmorMiddleware with your secret key and optional configurations
secret_key = b"12345678"  # do not hard code this! use secret or env variable
api_armor_middleware = APIArmorMiddleware(
    secret_key=secret_key, min_time_difference=60, ip_whitelist=["127.0.0.1"]
)

app.before_request(api_armor_middleware)


# Define a route that requires APIArmorMiddleware validation
@app.route("/protected", methods=["POST"])
def protected_route():
    return jsonify({"message": "Request successfully processed!"})


if __name__ == "__main__":
    app.run(debug=True)
