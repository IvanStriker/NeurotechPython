from typing import Any

from LaboratoryWork8.src.utils.decorators import check_types
from .author import Author


class App:
    """
    Represents an application with name,
    version, and author information.

    Attributes:
        name (str): The name of the application.
        version (str): The version number of the application.
        author (Author): The author of the application.
    """

    @check_types(Any, str, str, Author)
    def __init__(self, name: str, version: str, author: Author):
        """
        Initializes a new App instance.

        Args:
            name (str): The name of the application.
                Must be at least 2 characters
                long and mustn't consist entirely of digits.
            version (str): The version number of the application.
                Must contain only digits and dots.
            author (Author): The author of the application.

        Raises:
            ValueError: If name or version does not fit
                validation criteria.
        """
        self.name = name
        self.version = version
        self.author = author

    @property
    def name(self) -> str:
        """
        Gives back the application name.

        Returns:
            str: The current name of the application.
        """
        return self.__name

    @name.setter
    @check_types(Any, str)
    def name(self, name: str) -> None:
        """
        Sets the application name with validation.

        Args:
            name (str): The new name for the application.
                Must be at least 2 characters long and
                not consist entirely of digits.

        Raises:
            ValueError: If name is 1 character or less, or
                consists entirely of digits.
        """
        if len(name) <= 1 or all(i.isdigit() for i in name):
            raise ValueError(
                f"App.name: invalid name for application {name}"
            )
        self.__name = name

    @property
    def version(self) -> str:
        """
        Gets the application version.

        Returns:
            str: The current version number of the application.
        """
        return self.__version

    @version.setter
    @check_types(Any, str)
    def version(self, version: str) -> None:
        """
        Sets the application version with validation.

        Args:
            version (str): The new version number for the application.
                Must contain only digits and dots.

        Raises:
            ValueError: If version is empty or contains characters
                other than digits and dots.
        """
        if len(version) < 1 or any(not i.isdigit() and i != '.'
                                   for i in version):
            raise ValueError(
                f"App.name: invalid version for application {version}"
            )
        self.__version = version

    @property
    def author(self) -> Author:
        """
        Gets the application author.

        Returns:
            Author: The current author of the application.
        """
        return self.__author

    @author.setter
    @check_types(Any, Author)
    def author(self, author: Author) -> None:
        """
        Sets the application author.

        Args:
            author (Author): The new author for the application.
        """
        self.__author = author
