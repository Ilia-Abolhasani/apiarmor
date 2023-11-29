# API Armor

APIArmor is a Python package designed to enhance the security of API communication. It provides server-side middleware for Flask applications and client-side utilities to ensure secure, timestamped, and hash-verified data exchanges.

## Features

- **Server-Side Middleware:** Protect your Flask API with APIArmorMiddleware, adding time-based and hash verification to incoming requests.

- **Client-Side Utilities:** Utilize client-side functions for secure data hashing and sending to APIArmor-protected servers.

## Installation

```bash
pip install apiarmor
```

## Server-Side Usage
```python
from flask import Flask
from apiarmor.server.middleware import APIArmorMiddleware

app = Flask(__name__)

secret_key = b'your_secret_key'
api_armor_middleware = APIArmorMiddleware(secret_key=secret_key)
app.before_request(api_armor_middleware)

# Define your routes...
```
## Client-Side Usage
```python
from apiarmor_client import ApiArmorClient
```
## Contributing
Contributions are welcome! If you find a bug or have a suggestion, please open an issue.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## ⚠️ Security Notice

**Important:** Ensure the secure handling of your API keys and secrets. Do not hard code sensitive information directly in your source code. Consider using environment variables or a secure configuration management system to store and retrieve confidential data.

For example, you can use the `python-decouple` library along with a `.env` file to manage your project's configuration:

1. Install `python-decouple`:

    ```bash
    pip install python-decouple
    ```

2. Create a `.env` file in your project's root directory and add your secret information:

    ```ini
    SECRET_KEY=your_actual_secret_key
    ```

3. In your code, use `python-decouple` to access your configuration variables:

    ```python
    from decouple import config

    secret_key = config('SECRET_KEY')
    ```

By following secure practices, you help protect your application and sensitive data.
