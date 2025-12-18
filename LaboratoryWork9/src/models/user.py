from typing import Any

from LaboratoryWork9.src.utils.decorators import check_types
from .human import Human
from .base_model import BaseModel


class User(BaseModel, Human):
    """
    Represents a user combining identification and human attributes.

    Inherits from both BaseModel (for ID) and
    Human (for name with validation).
    """

    @check_types(Any, int, str)
    def __init__(self, id: int, name: str):
        """
        Initializes a new User instance with ID and name.

        Args:
            id (int): Unique identifier from BaseModel.
            name (str): User's name from Human.
                Must be at least 2 characters long and
                not consist entirely of digits.
        """
        Human.__init__(self, name)
        BaseModel.__init__(self, id)

    def parseDict(self) -> dict[str, Any]:
        return {"name": self.name} | BaseModel.parseDict(self)