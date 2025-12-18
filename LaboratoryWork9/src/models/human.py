from typing import Any

from LaboratoryWork9.src.utils.decorators import check_types


class Human:
    """
    Represents a human with a validated name property.

    Base class for entities that require name validation
    with specific rules.
    """

    @check_types(Any, str)
    def __init__(self, name: str):
        """
        Initializes a new Human instance with a name.

        Args:
            name (str): The name of the human. Must be at least
                2 characters long and not consist entirely of digits.

        Raises:
            ValueError: If name does not fit validation criteria.
        """
        self.name = name

    @property
    def name(self) -> str:
        """
        Gets the human's name.

        Returns:
            str: The current name of the human.
        """
        return self.__name

    @name.setter
    @check_types(Any, str)
    def name(self, name: str) -> None:
        """
        Sets the human's name with validation.

        Args:
            name (str): The new name for the human.
                Must be at least 2 characters long
                and not consist entirely of digits.

        Raises:
            ValueError: If name is 1 character or less,
                or consists entirely of digits. Error message
                includes class name.
        """
        if len(name) <= 1 or all(i.isdigit() for i in name):
            raise ValueError(
                f"{self.__class__}.name: invalid name "
                f"for {self.__class__} {name}"
            )
        self.__name = name