from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.model.movie import Movie


class MovieService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if model := self.dao.get_by_id(pk):
            return model
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_all(page=page)

    # def get_all_with_filters(self, filters) -> list[Movie]:
    #     return self.dao.get_all_with_filters(filters)

    # def get_all_movies(self, data):
    #     movies_query = self.dao.get_all()
    #     status = data.get('status')
    #     page = data.get('page')

    #     if status and status == 'new':
    #         movies_query = self.dao.get_new(movies_query)
