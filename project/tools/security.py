import base64
import hashlib
import jwt

from flask import current_app, request


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            return {"error": "Not authorize request"}, 401
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            validate_token(token)
        except Exception as e:
            print(f"Traceback: {e}")
            return {"error": "Not authorize request"}, 401
        return func(*args, **kwargs)

    return wrapper


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def validate_token(token: str) -> None:
    jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=[current_app.config["PWD_HASH_ALGO"]])


# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)
