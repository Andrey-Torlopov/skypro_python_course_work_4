import calendar
import datetime
import base64
import hashlib

import hmac
import jwt
from flask import request, current_app

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.model.user import User
from project.services import UserService
from project.tools.security import generate_password_hash

class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def auth_user(self, email, password):
        user = self.user_service.get_user_by_email(email)

        if user is None:
            return {"error": "Пользователь не существует"}, 401

        if user.password != generate_password_hash(password):
            return {"error": "Пароли не совпадают"}, 401

        return self._generate_token(email)


    def refresh_token(self, refresh_token: str):
        """
        Обновляем токены и возращаем новую пару access_token, refresh_token
        """
        try:
            data = jwt.decode(jwt=refresh_token, key=current_app.config["SECRET_KEY"], algorithms=[current_app.config["PWD_HASH_ALGO"]])
        except Exception as e:
            return {"error": "Bad request"}, 400

        email = data.get("email")

        user = self.user_service.get_user_by_email(email)
        if user is None:
            return {"error": "Bad request"}, 400

        return self._generate_token(user.email)


    def compare_passwords(self, password_hash, other_password_hash) -> bool:
        decoded_digest = base64.b64decode(password_hash)
        other_decoded_password = base64.b64decode(other_password_hash)
        return hmac.compare_digest(decoded_digest, other_decoded_password)

    # Private

    def _generate_token(self, email: str) -> dict[str, str]:
        data = {"email": email}

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = self._jwt_encode_data(data)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = self._jwt_encode_data(data)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens

    def _jwt_encode_data(self, data: dict[str, str]) -> dict[str, str]:
        token = jwt.encode(data, current_app.config["SECRET_KEY"], current_app.config["PWD_HASH_ALGO"])
        print("<<< 111")
        return token
