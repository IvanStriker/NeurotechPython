from typing import Any

from LaboratoryWork9.src.models import UserCurrency, Currency
from LaboratoryWork9.src.utils.currencies_api import get_currencies
from LaboratoryWork9.src.controllers.crud import *
from LaboratoryWork9.src.utils.decorators import check_types


class CurrencyController:
    """
    Currency and subscription objects controller providing
     us with high-level sqlite API
    """
    def __init__(self, currencyCRUD: CurrencyCRUD = CurrencyCRUD(),
                 subscriptionCRUD: CurrencyCRUD = CurrencyCRUD()):
        """
        Initializing inner Currency and Subscription cruds

        Args:
            currencyCRUD (CurrencyCRUD): Specific middle-level
                currency-crud to run the commands through
            subscriptionCRUD (UserCurrencyCRUD): Specific
                middle-level subscription-crud to run
                the commands through
        """
        self.__currency = currencyCRUD
        self.__subscription = subscriptionCRUD

    def __reload(self):
        """
        Reloads currency data from bank's API
        See utils.get_currencies
        """
        newData = [val for key, val in get_currencies().items()]
        ids = [item.char_code for item in newData]
        takenInAccount = {val.id for val in self.__currency.readAll()}
        for i in range(len(ids)):
            if newData[i].id in takenInAccount:
                self.__currency.update("char_code", ids[i], newData[i])
            else:
                self.__currency.create(newData[i])

    def getAll(self) -> list[Currency]:
        """
        Gives back all the currencies received
         with bank's API

        Returns:
            List: The list of all the currencies.
        """
        self.__reload()
        return self.__currency.readAll()

    @check_types(Any, int)
    def get(self, id: int) -> Currency:
        """
        Gives back a currency by its ID
         after reloading the data from bank's API.

        Args:
            id (int): The currency's id.

        Returns:
            Currency: The currency found.
        """
        self.__reload()
        return self.__currency.read("id", id)

    @check_types(Any, int)
    def getForUser(self, userID: int) -> list[Currency]:
        """
        Gives back the currencies
         subscribed by a particular user.

        Args:
            userID (int): User identifier.

        Returns:
            list: The list of currencies
             subscribed by the user given.
        """
        currencies = [item.currency_id for item in
                      self.__subscription.readAll("user_id", [userID])]
        return self.__currency.readAll("id", currencies)

    @check_types(Any, UserCurrency)
    def subscribe(self, subscription: UserCurrency):
        """
        Adds a new currency subscription for a user.

        Args:
            subscription (UserCurrency): Subscription
                object to add.
        """
        self.__subscription.create(subscription)

    @check_types(Any, str, float|int)
    def updateCurrency(self, char_name: str, value: float) -> Currency:
        """
        Updates a currency rate by its character code.

        Args:
            char_name (str): Currency character code.
            value (float): New currency rate.

        Returns:
            Updated currency object.
        """
        curr = self.__currency.read("char_code", char_name)
        curr.value = value
        self.__currency.update("char_code", char_name, curr)
        return curr

    @check_types(Any, int)
    def deleteCurrency(self, id: int) -> Currency:
        """
        Deletes a currency given by ID.

        Args:
            id (int): Currency identifier.

        Returns:
            Currency: The deleted currency object.
        """
        curr = self.__currency.read("id", id)
        self.__currency.delete("id", id)
        return curr
