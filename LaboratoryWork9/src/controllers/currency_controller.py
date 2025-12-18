from typing import Any

from LaboratoryWork9.src.models import UserCurrency, Currency
from LaboratoryWork9.src.utils.currencies_api import get_currencies
from LaboratoryWork9.src.controllers.crud import *
from LaboratoryWork9.src.utils.decorators import check_types


class CurrencyController:
    def __init__(self):
        self.__currency = CurrencyCRUD()
        self.__subscription = UserCurrencyCRUD()

    def __reload(self):
        newData = [val for key, val in get_currencies().items()]
        ids = [item.char_code for item in newData]
        takenInAccount = {val.id for val in self.__currency.readAll()}
        for i in range(len(ids)):
            if newData[i].id in takenInAccount:
                self.__currency.update("char_code", ids[i], newData[i])
            else:
                self.__currency.create(newData[i])

    def getAll(self) -> list[Currency]:
        self.__reload()
        return self.__currency.readAll()

    @check_types(Any, int)
    def get(self, id: int) -> Currency:
        self.__reload()
        return self.__currency.read("id", id)

    @check_types(Any, int)
    def getForUser(self, userID: int) -> list[Currency]:
        currencies = [item.currency_id for item in
                      self.__subscription.readAll("id", [userID])]
        return self.__currency.readAll("id", currencies)

    @check_types(Any, UserCurrency)
    def subscribe(self, subscription: UserCurrency):
        self.__subscription.create(subscription)
