from typing import Any

from LaboratoryWork8.src.utils.decorators import check_types
from .base_model import BaseModel


class UserCurrency(BaseModel):
    """
    Represents a relationship between a user and a currency.

    Acts as a junction/association class linking
    User and Currency entities through their IDs.
    """

    @check_types(Any, str, str, str)
    def __init__(self, id: str, user_id: str, currency_id: str):
        """
        Initializes a new UserCurrency relationship instance.

        Args:
            id (str): Unique id for this relationship
                from BaseModel.
            user_id (str): id of the associated User.
            currency_id (str): id of the associated Currency.
        """
        BaseModel.__init__(self, id)
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def user_id(self) -> str:
        """
        Gets the user's id.

        Returns:
            str: The id of the user in this relationship.
        """
        return self.__user_id

    @user_id.setter
    @check_types(Any, str)
    def user_id(self, user_id: str) -> None:
        """
        Sets the associated user's id.

        Args:
            user_id (str): The new user id for
                this relationship.
        """
        self.__user_id = user_id

    @property
    def currency_id(self) -> str:
        """
        Gets the associated currency's id.

        Returns:
            str: The id of the currency in this relationship.
        """
        return self.__currency_id

    @currency_id.setter
    @check_types(Any, str)
    def currency_id(self, currency_id: str) -> None:
        """
        Sets the currency's id.

        Args:
            currency_id (str): The new currency id for this
                relationship.
        """
        self.__currency_id = currency_id