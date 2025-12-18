from typing import Any

from LaboratoryWork9.src.utils.decorators import check_types
from .human import Human


class Author(Human):
    """
    Represents an author who is a human with an associated group.

    Inherits from Human and adds group information with validation.
    """

    @check_types(Any, str, str)
    def __init__(self, name: str, group: str):
        """
        Initializes a new Author instance.

        Args:
            name (str): The name of the author. Inherited from
                Human class.
            group (str): The group identifier for the author.
                Must be at least 5 characters long and start
                with an uppercase letter.

        Raises:
            ValueError: If group does not fit the validation
                criteria.
        """
        Human.__init__(self, name)
        self.group = group

    @property
    def group(self) -> str:
        """
        Gets the author's group identifier.

        Returns:
            str: The current group identifier of the author.
        """
        return self.__group

    @group.setter
    @check_types(Any, str)
    def group(self, group: str) -> None:
        """
        Sets the author's group identifier with validation.

        Args:
            group (str): The new group identifier. Must be
                at least 5 characters long and start
                with an uppercase letter (A-Z).

        Raises:
            ValueError: If group is less than 5 characters
                or does not start with an uppercase letter.
        """
        if len(group) < 5 or not (ord('A') <= ord(group[0]) <= ord('Z')):
            raise ValueError(
                f"Author.group: invalid group for author: {group}"
            )
        self.__group = group