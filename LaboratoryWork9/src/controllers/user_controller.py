from typing import Any

from LaboratoryWork9.src.controllers.crud import *
from LaboratoryWork9.src.models import User
from LaboratoryWork9.src.utils.decorators import check_types


class UserController:
    def __init__(self):
        self.__user = UserCRUD()

    def getAll(self) -> list[User]:
        return self.__user.readAll()

    @check_types(Any, int)
    def get(self, userID: int) -> User:
        return self.__user.read("id", userID)

    @check_types(Any, str)
    def getByName(self, name: str) -> User:
        return self.__user.read("name", name)

    @check_types(Any, User)
    def add(self, user: User):
        self.__user.create(user)