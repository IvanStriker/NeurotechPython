from typing import Any

from LaboratoryWork9.src.utils.decorators import check_types
from .base_model import BaseModel


class UserCurrency(BaseModel):
    """
    Represents a relationship between a user and a currency.

    Acts as a junction/association class linking
    User and Currency entities through their IDs.
    """

    @check_types(Any, int, int, int)
    def __init__(self, id: int, user_id: int, currency_id: int):
        """
        Initializes a new UserCurrency relationship instance.

        Args:
            id (int): Unique id for this relationship
                from BaseModel.
            user_id (int): id of the associated User.
            currency_id (int): id of the associated Currency.
        """
        BaseModel.__init__(self, id)
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def user_id(self) -> int:
        """
        Gets the user's id.

        Returns:
            str: The id of the user in this relationship.
        """
        return self.__user_id

    @user_id.setter
    @check_types(Any, int)
    def user_id(self, user_id: int) -> None:
        """
        Sets the associated user's id.

        Args:
            user_id (int): The new user id for
                this relationship.
        """
        self.__user_id = user_id

    @property
    def currency_id(self) -> int:
        """
        Gets the associated currency's id.

        Returns:
            int: The id of the currency in this relationship.
        """
        return self.__currency_id

    @currency_id.setter
    @check_types(Any, int)
    def currency_id(self, currency_id: int) -> None:
        """
        Sets the currency's id.

        Args:
            currency_id (int): The new currency id for this
                relationship.
        """
        self.__currency_id = currency_id

    def parseDict(self) -> dict[str, Any]:
        return {
            "user_id": self.__user_id,
            "currency_id": self.currency_id
        } | BaseModel.parseDict(self)