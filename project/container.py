from project.dao import GenresDAO
from project.dao import DirectorDAO
from project.dao import MovieDAO
from project.dao import UserDAO

from project.services import GenresService
from project.services import DirectorService
from project.services import MovieService
from project.services import UserService
from project.services import AuthService

from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)