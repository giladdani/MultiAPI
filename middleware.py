from flask import Response, request
from functools import wraps
from dotenv import load_dotenv
import os
load_dotenv()


def auth_api_key(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        api_key = request.headers["authorization"]
        if api_key == os.environ["API_KEY"]:
            return func(*args, **kwargs)

        return Response("Authorization failed", mimetype="text/plain", status=401)
    return decorated_function