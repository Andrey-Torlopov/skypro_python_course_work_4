from project.dao.base import BaseDAO
from project.dao.model.user import User


class UserDAO(BaseDAO[User]):
    __model__ = User

    def create(self, data):
        ent = User(**data)
        self._db_session.add(ent)
        self._db_session.commit()
        return ent

    def delete(self, uid):
        user = self.get_by_id(uid)
        self._db_session.delete(user)
        self._db_session.commit()

    def update(self, data):
        user = self.get_by_id(data.get("id"))
        user.name = data.get("email")
        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favorite_genre = data.get("favorite_genre")

        self._db_session.add(user)
        self._db_session.commit()

    def get_user_by_email(self, email: str):
        return self._db_session.query(User).filter(User.email == email).first()
