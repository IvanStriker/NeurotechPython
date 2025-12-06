from typing import Any

from LaboratoryWork8.src.utils.decorators import check_types


class BaseModel:
    """
    Base class for models providing a unique identifier.

    Serves as a foundation for other model classes that require an ID.
    """

    @check_types(Any, str)
    def __init__(self, id: str):
        """
        Initializes a new BaseModel instance with an identifier.

        Args:
            id (str): The unique identifier for the model instance.
        """
        self.id = id

    @property
    def id(self) -> str:
        """
        Gets the model's unique identifier.

        Returns:
            str: The current identifier of the model instance.
        """
        return self.__id

    @id.setter
    @check_types(Any, str)
    def id(self, id: str) -> None:
        """
        Sets the model's unique identifier.

        Args:
            id (str): The new identifier for the model instance.
        """
        self.__id = id