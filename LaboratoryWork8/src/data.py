import threading

from jinja2 import Environment, PackageLoader, select_autoescape

from typing import Callable, Any
import LaboratoryWork8.src.models as models
import LaboratoryWork8.src.utils.currencies_api as currency


templates: dict[str, Any] = {}

author: models.Author = models.Author("Ivan Vinogradov", "P3121")
app: models.App = models.App("Currency", "1.1", author)
users: dict[str, models.User] = {
    "0": models.User("0", "Ivan Vinogradov")
}
currencies: dict[str, models.Currency] = {}
subscriptions: dict[str, models.UserCurrency] = {}

mutex: threading.Lock = threading.Lock()


def load_templates():
    """
    Initializes and loads templates.
    Creates Jinja2 Environment
    """
    env = Environment(
        loader=PackageLoader("myapp"),
        autoescape=select_autoescape()
    )
    global templates
    templates["index"] = env.get_template("index.html")
    templates["users"] = env.get_template("users.html")
    templates["currencies"] = env.get_template("currencies.html")
    templates["signUp"] = env.get_template("signUp.html")
    templates["login"] = env.get_template("login.html")
    templates["author"] = env.get_template("author.html")


def load_currencies():
    """
    Prepares currency list using the bank API
    """
    with mutex:
        global currencies
        currencies = currency.get_currencies()


def addUser(user: models.User):
    """
    Adds a new user to the global users dictionary

    Args:
        user (models.User): The User object to add
    """
    with mutex:
        global users
        users[user.id] = user


def addSubscription(subscription: models.UserCurrency):
    """
    Adds a currency subscription for a user

    Args:
        subscription (models.UserCurrency): The UserCurrency
            object to add
    """
    with mutex:
        global subscriptions
        subscriptions[subscription.id] = subscription


def load_data():
    """
    Initializes all data needed for application's working
    """
    load_templates()
    load_currencies()