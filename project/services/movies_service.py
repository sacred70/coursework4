from typing import Optional

from project.models import Movie
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status: Optional[int] = None) -> list[Movie]:
        return self.dao.get_all(page=page, status=status)
