from typing import Any

from LaboratoryWork9.src.utils.decorators import check_types


class BaseModel:
    """
    Base class for models providing a unique identifier.

    Serves as a foundation for other model classes that require an ID.
    """

    @check_types(Any, int)
    def __init__(self, id: int):
        """
        Initializes a new BaseModel instance with an identifier.

        Args:
            id (int): The unique identifier for the model instance.
        """
        self.id = id

    @property
    def id(self) -> int:
        """
        Gets the model's unique identifier.

        Returns:
            int: The current identifier of the model instance.
        """
        return self.__id

    @id.setter
    @check_types(Any, int)
    def id(self, id: int) -> None:
        """
        Sets the model's unique identifier.

        Args:
            id (int): The new identifier for the model instance.
        """
        self.__id = id

    def parseDict(self) -> dict[int, Any]:
        """
        Turn the current object into a dict
        of its viable attributes

        Returns:
            Dict[str, Any]: A dict of the object's attributes
        """
        return {"id": self.__id}