from project.dao.base import BaseDAO
from project.dao.model.movie import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    # def get_by_director_id(self, uid):
    #     return self._db_session.query(Movie).filter(Movie.director_id == uid).all()

    # def get_by_genre_id(self, uid):
    #     return self._db_session.query(Movie).filter(Movie.genre_id == uid).all()

    # def get_by_year(self, year):
    #     return self._db_session.query(Movie).filter(Movie.year == year).all()

    def get_new(self, query) -> list[Movie]:

        return []

    def get_pages(self):
        ...

    # def get_all_with_filters(self, filters):
    #     query = self._db_session.query(Movie)
    #     director_id = filters.get('director_id')
    #     genre_id = filters.get('genre_id')
    #     year = filters.get('year')

    #     if director_id is not None:
    #         query = query.filter(Movie.director_id == director_id)

    #     if genre_id is not None:
    #         query = query.filter(Movie.genre_id == genre_id)

    #     if year is not None:
    #         query = query.filter(Movie.year == year)

    #     return query.all()
