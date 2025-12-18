from jinja2 import Environment, PackageLoader, select_autoescape

from typing import Any
import LaboratoryWork9.src.models as models
from LaboratoryWork9.src.controllers.currency_controller import CurrencyController
from LaboratoryWork9.src.controllers.user_controller import UserController

templates: dict[str, Any] = {}

author: models.Author = models.Author("Ivan Vinogradov", "P3121")
app: models.App = models.App("Currency", "1.1", author)

users = UserController()
currencies = CurrencyController()


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


def addUser(user: models.User):
    """
    Adds a new user to the global users dictionary

    Args:
        user (models.User): The User object to add
    """
    global users
    users.add(user)


def addSubscription(subscription: models.UserCurrency):
    """
    Adds a currency subscription for a user

    Args:
        subscription (models.UserCurrency): The UserCurrency
            object to add
    """
    global currencies
    currencies.subscribe(subscription)


def load_data():
    """
    Initializes all data needed for application's working
    """
    load_templates()