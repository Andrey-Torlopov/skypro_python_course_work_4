from typing import Optional
import base64
import hashlib

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.model.user import User
from project.config import config

from project.tools.security import generate_password_hash, compare_passwords

class UserService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_one(self, pk: int) -> User:
        if model := self.dao.get_by_id(pk):
            return model
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    def create(self, data: dict[str, str]):
        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            return {"error": "Bad request"}, 400

        user = self.get_user_by_email(email)
        if user is not None:
            return {"error": "Пользователь уже суещствует."}, 401

        user_data = {
            "email": email,
            "password": generate_password_hash(password)
        }
        return self.dao.create(user_data)

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_user_by_email(self, email: str):
        return self.dao.get_user_by_email(email)

    def  patch(self, data):
        self.dao.update(data)

    def update_password(self, data: dict[str, str]):
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        uid = data.get('id')

        if None in [old_password, new_password, uid]:
            return  {'error': 'Not enough data'}, 401

        user = self.dao.get_by_id(uid)
        if user is None:
            return {'error': 'User not found'}, 401

        old_password_hash = generate_password_hash(old_password)

        if compare_passwords(user.password, old_password_hash) == False:
            return {'error': 'Password is incorrect'}, 401

        new_hashed_password = generate_password_hash(new_password)
        self.dao.update_password(uid, new_hashed_password)

