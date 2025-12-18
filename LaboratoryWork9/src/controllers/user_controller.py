from typing import Any

from LaboratoryWork9.src.controllers.crud import *
from LaboratoryWork9.src.models import User
from LaboratoryWork9.src.utils.decorators import check_types


class UserController:
    """
    User objects controller providing us with high-level
     sqlite API
    """
    def __init__(self, userCRUD: UserCRUD = UserCRUD()):
        """
        Initializing inner crud object

        Args:
            userCRUD (UserCRUD): Specific middle-level
                user-crud to run the commands through
        """
        self.__user = userCRUD

    def getAll(self) -> list[User]:
        """
        Gives back all the users.

        Returns:
            list: The lList of all users.
        """
        return self.__user.readAll()

    @check_types(Any, int)
    def get(self, userID: int) -> User:
        """
        Gives back a user by its ID.

        Args:
            userID (int): User's id.

        Returns:
            User: The user found.
        """
        return self.__user.read("id", userID)

    @check_types(Any, str)
    def getByName(self, name: str) -> User:
        """
        Gives back a user by its name.

        Args:
            name (str): User's name.

        Returns:
            User: The user found.
        """
        return self.__user.read("name", name)

    @check_types(Any, User)
    def add(self, user: User):
        """
        Adds a new user.

        Args:
            user (User): User object to add.
        """
        self.__user.create(user)