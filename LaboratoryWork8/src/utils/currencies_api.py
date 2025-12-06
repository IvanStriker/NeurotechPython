import json

import requests

from .decorators import logger
from logging import getLogger
from LaboratoryWork8.src.models.currency import Currency
from .decorators import check_types

basicAddress: str = "https://www.cbr-xml-daily.ru/daily_json.js"
logFile = getLogger("logs")


@logger(handle=logFile)
@check_types(list|None, str)
def get_currencies(currency_codes: list = None,
                   url: str = basicAddress) -> dict:
    """
    Gets currency rates from the central Russian bank

    Args:
        currency_codes (list): The list of the short
            currency codes: "USD", "EUR", ...
        url (str): The url address to the bank API

    Returns:
        dict: The dict, where the keys are currencies' ids
            and values are objects of Currency class
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.ConnectionError(
            f"get_currencies: unable to connect...\n{e.__str__()}"
        )

    try:
        data = response.json()
    except json.JSONDecodeError as e:
        raise ValueError(
            f"get_currencies: unable to parse "
            f"received data to json...\n{e.__str__()}"
        )

    currencies = {}

    try:
        received_currency: dict = data["Valute"]
    except KeyError as e:
        raise KeyError(
            f"get_currency: haven't received any currency info..."
            f"\n{e.__str__()}"
        )

    source = currency_codes if currency_codes else received_currency
    for code in source:
        try:
            currencies[received_currency[code]["ID"]] = Currency(
                id=received_currency[code]["ID"],
                name=received_currency[code]["Name"],
                value=float(received_currency[code]["Value"]),
                char_code=received_currency[code]["CharCode"],
                num_code=int(received_currency[code]["NumCode"]),
                nominal=int(received_currency[code]["Nominal"])
            )
        except KeyError as e:
            raise KeyError(
                f"get_currency: received no info about {code}...\n"
                f"{e.__str__()}"
            )
        except ValueError as e:
            raise ValueError(
                f"get_currency: can't parse to float "
                f"{received_currency[code]["Value"]}..."
                f"{e.__str__()}"
            )
    return currencies
    # raise requests.exceptions.RequestException('Упали с исключением')
