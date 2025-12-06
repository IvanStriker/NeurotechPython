import threading
import uuid

from jinja2 import Environment, PackageLoader, select_autoescape

from typing import Callable, Any
import models
import utils.currencies_api as currency


templates: dict[str, Any] = {}

author: models.Author = models.Author("Ivan Vinogradov", "P3121")
app: models.App = models.App("Currency", "1.1", author)
users: dict[str, models.User] = {}
currencies: dict[str, models.Currency] = {}
subscriptions: dict[str, models.UserCurrency] = {}

mutex: threading.Lock = threading.Lock()


def load_templates():
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


def load_currencies():
    with mutex:
        global currencies
        currencies = currency.get_currencies()


def addUser(user: models.User):
    with mutex:
        global users
        users[user.id] = user


def addSubscription(subscription: models.UserCurrency):
    with mutex:
        global subscriptions
        subscriptions[subscription.id] = subscription


def load_data():
    load_templates()
    load_currencies()