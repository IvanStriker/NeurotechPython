import LaboratoryWork8.src.data as data
import LaboratoryWork8.src.models as models

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


@check_types(models.User)
def profile(user: models.User):
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
                    "id": val.user_id,
                    "name": data.users[val.user_id].name
                },
                "currency": {
                    "charCode":
                        data.currencies[val.currency_id].char_code,
                    "value":
                        data.currencies[val.currency_id].value
                }
            }
            for key, val in data.subscriptions.items()
            if val.user_id == user.id
        ]
    )


def users():
    """
    Renders the users page.

    Returns:
        str: the page
    """
    return data.templates["users"].render(
        **baseTemplateKwargs,
        users=[{"name": user.name, "id": user.id}
               for user in data.users.values()]
    )


def currencies():
    """
    Renders the currencies page.

    Returns:
        str: the page
    """
    return data.templates["currencies"].render(
        **baseTemplateKwargs,
        currencies=[cur.parseDict()
                    for id, cur in data.currencies.items()]
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