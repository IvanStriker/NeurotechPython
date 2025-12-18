import LaboratoryWork9.src.data as data
import LaboratoryWork9.src.models as models
from LaboratoryWork9.src.models import Currency

from utils.decorators import check_types


baseTemplateKwargs = {
    "myapp": data.app.name,
    "navigation": [
        {"href": "/", "caption": "Главная"},
        {"href": "/login", "caption": "Войти"},
        {"href": "/signUp", "caption": "Зарегистрироваться"},
        {"href": "/user", "caption": "Профиль"},
        {"href": "/currencies", "caption": "Курсы валют"},
        {"href": "/users", "caption": "Пользователи"},
    ],
    "author": data.author.name,
    "group": data.author.group,
    "contacts": {
        "email": "vinogradovivan548@gmail.com",
        "phone": "+7-904-618-93-84"
    }
}


def root():
    """
    Renders the root page.

    Returns:
        str: the page
    """
    return data.templates["index"].render(
        **baseTemplateKwargs,
        currencies=[],
    )


@check_types(models.User, list)
def profile(user: models.User,
            currencies: list[models.Currency]):
    """
    Renders the user profile page

    Args:
        user (models.User): The User object whose
            profile to render.

    Returns:
        str: the page
    """
    return data.templates["index"].render(
        **baseTemplateKwargs,
        user={
            "id": user.id,
            "name": user.name
        },
        subscriptions=[
            {
                "user": {
                    "id": user.id,
                    "name": user.name
                },
                "currency": {
                    "charCode":
                        val.char_code,
                    "value":
                        val.value
                }
            }
            for val in currencies
        ]
    )


@check_types(list)
def users(users: list[models.User]):
    """
    Renders the users page.

    Args:
        users (List[User]) - The list of users to display

    Returns:
        str: the page
    """
    return data.templates["users"].render(
        **baseTemplateKwargs,
        users=users
    )


@check_types(list)
def currencies(currencies: list[Currency]):
    """
    Renders the currencies page.

    Returns:
        str: the page
    """
    return data.templates["currencies"].render(
        **baseTemplateKwargs,
        currencies=[cur.parseDict()
                    for id, cur in currencies]
    )


def signUp():
    """
    Renders the user registration page.

    Returns:
        str: the page
    """
    return data.templates["signUp"].render(
        **baseTemplateKwargs
    )


def login():
    """
    Renders the user login page.

    Returns:
        str: the page
    """
    return data.templates["login"].render(
        **baseTemplateKwargs
    )


def author():
    """
    Renders the author information page.

    Returns:
        str: the page
    """
    return data.templates["author"].render(
        **baseTemplateKwargs
    )