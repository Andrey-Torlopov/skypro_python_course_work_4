from .auth import auth_ns, user_ns
from .genre import genres_ns
from .movie import movies_ns
from .director import director_ns

__all__ = [
    'auth_ns',
    'genres_ns',
    'user_ns',
    'movies_ns',
    'director_ns'
]
