from typing import Any

from LaboratoryWork9.src.utils.decorators import check_types
from .base_model import BaseModel


class Currency(BaseModel):
    """
    Represents a currency with code, name, value,
    and nominal information.

    Inherits from BaseModel and adds currency-specific
    properties with validation for financial applications.
    """

    @check_types(Any, int, str, str, str, float | int, int)
    def __init__(self, id: int, num_code: str,
                 char_code: str, name: str, value: float,
                 nominal: int):
        """
        Initializes a new Currency instance.

        Args:
            id (int): Unique identifier from BaseModel.
            num_code (str): Numeric code of the currency
            char_code (str): 3-character currency code
            name (str): Full name of the currency
            value (float): Current value/rate of the currency.
                Must be positive.
            nominal (int): Nominal value/unit for the rate.
                Must be positive.

        Raises:
            ValueError: If char_code is not 3 characters,
                name is empty, or value/nominal are not positive.
        """
        BaseModel.__init__(self, id)
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def num_code(self) -> str:
        """
        Gets the currency's numeric code.

        Returns:
            str: The numeric code of the currency.
        """
        return self.__num_code

    @num_code.setter
    @check_types(Any, str)
    def num_code(self, num_code: str):
        """
        Sets the currency's numeric code.

        Args:
            num_code (str): The new numeric code for the currency.
        """
        self.__num_code = num_code

    @property
    def char_code(self) -> str:
        """
        Gets the currency's 3-character code.

        Returns:
            str: The 3-character currency code (e.g., 'USD', 'EUR').
        """
        return self.__char_code

    @char_code.setter
    @check_types(Any, str)
    def char_code(self, char_code: str) -> None:
        """
        Sets the currency's 3-character code with validation.

        Args:
            char_code (str): The new 3-character currency code.

        Raises:
            ValueError: If char_code length is not exactly 3 characters.
        """
        if len(char_code) != 3:
            raise ValueError(
                f"Currency.char_code: invalid char_code for currency: "
                f"{char_code}"
            )
        self.__char_code = char_code

    @property
    def name(self) -> str:
        """
        Gets the currency's full name.

        Returns:
            str: The full name of the currency.
        """
        return self.__name

    @name.setter
    @check_types(Any, str)
    def name(self, name: str) -> None:
        """
        Sets the currency's full name with validation.

        Args:
            name (str): The new full name for the currency.

        Raises:
            ValueError: If name is an empty string.
        """
        if name == "":
            raise ValueError(
                f"Currency.name: invalid name for currency: "
                f"{name}"
            )
        self.__name = name

    @property
    def value(self) -> float:
        """
        Gets the currency's current value/rate.

        Returns:
            float: The current value/rate of the currency.
        """
        return self.__value

    @value.setter
    @check_types(Any, float | int)
    def value(self, value: float) -> None:
        """
        Sets the currency's value/rate with validation.

        Args:
            value (float | int): The new value/rate for the currency.

        Raises:
            ValueError: If value is not positive (<= 0).
        """
        if value <= 0:
            raise ValueError(
                f"Currency.value: invalid value for currency: "
                f"{value}"
            )
        self.__value = value

    @property
    def nominal(self) -> int:
        """
        Gets the currency's nominal value.

        Returns:
            int: The nominal value/unit for the currency rate.
        """
        return self.__nominal

    @nominal.setter
    @check_types(Any, int)
    def nominal(self, nominal: int) -> None:
        """
        Sets the currency's nominal value with validation.

        Args:
            nominal (int): The new nominal value for the currency.

        Raises:
            ValueError: If nominal is not positive (<= 0).
        """
        if nominal <= 0:
            raise ValueError(
                f"Currency.value: invalid nominal for currency: "
                f"{nominal}"
            )
        self.__nominal = nominal

    def parseDict(self) -> dict[str, Any]:
        """
        Converts the currency object to a dictionary representation.

        Returns:
            dict[str, Any]: Dictionary with currency
                properties including:
                - id: Unique identifier
                - name: Currency full name
                - charCode: 3-character code
                - value: Current value/rate
                - nominal: Nominal value
        """
        return {
            "name": self.name,
            "charCode": self.char_code,
            "value": self.value,
            "nominal": self.nominal,
        } | BaseModel.parseDict(self)