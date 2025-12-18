from LaboratoryWork9.src.utils import sessions

import LaboratoryWork9.src.data as data
from LaboratoryWork9.src.utils.decorators import check_types


@check_types(dict, sessions.Session)
def currencyUpdate(queryParams: dict[str, list[str]],
                   session: sessions.Session):
    """
    Handles the currency/update page request.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
        session (sessions.Session): Current user session.

    Returns:
        Updated currency.
    """
    currencyToUpdate = list(queryParams.items())
    updated = data.currencies.updateCurrency(
        currencyToUpdate[0][0],
        float(currencyToUpdate[0][1][0])
    )
    return f"{updated.parseDict()}"


@check_types(dict, sessions.Session)
def currencyDelete(queryParams: dict[str, list[str]],
                   session: sessions.Session):
    """
    Handles the currency/delete page request.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
        session (sessions.Session): Current user session.

    Returns:
        Deleted currency.
    """
    currencyToDel = list(queryParams.items())
    deleted = data.currencies.deleteCurrency(
        int(currencyToDel[0][1][0])
    )
    return f"{deleted.parseDict()}"


@check_types(dict, sessions.Session)
def currencyShow(queryParams: dict[str, list[str]],
                   session: sessions.Session):
    """
    Handles the currency/show page request.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
        session (sessions.Session): Current user session.

    Returns:
        Returns the entire currency list to load it into a view
         and prints it to the console.
    """
    currencyToShow = data.currencies.getAll()
    currencyToShow = [item.parseDict() for item in currencyToShow]
    print(currencyToShow)
    return f"{currencyToShow}"