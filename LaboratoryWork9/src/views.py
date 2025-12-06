import datetime
from typing import Callable, Any

import data
import models


baseTemplateKwargs = {
    "myapp": data.app.name,
    "navigation": [
        {"href": "/", "caption": "Главная"},
        {"href": "/login", "caption": "Войти"},
        {"href": "/signUp", "caption": "Зарегистрироваться"},
        {"href": "/profile", "caption": "Профиль"},
        {"href": "/currencies", "caption": "Курсы валют"},
    ],
    "author": data.author.name,
    "group": data.author.group,
    "contacts": {
        "email": "vinogradovivan548@gmail.com",
        "phone": "+7-904-618-93-84"
    }
}


def root():
    return data.templates["index"].render(
        **baseTemplateKwargs,
        currencies=[],
    )


def profile(user: models.User):
    print(data.currencies)
    return data.templates["index"].render(
        **baseTemplateKwargs,
        user={
            "id": user.id,
            "name": user.name
        },
        subscriptions=[
            {
                "currency": {
                    "value":
                        data.currencies[val.currency_id].value,
                    "charCode":
                        data.currencies[val.currency_id].char_code,
                    "nominal":
                        data.currencies[val.currency_id].nominal,
                }
            }
            for key, val in data.subscriptions.items()
            if val.user_id == user.id
        ]
    )


def users():
    return data.templates["users"].render(
        **baseTemplateKwargs,
        users=[{"name": user.name, "id": user.id}
               for user in data.users.values()]
    )


def currencies():
    return data.templates["currencies"].render(
        **baseTemplateKwargs,
        currencies=[cur.parseDict()
                    for id, cur in data.currencies.items()]
    )


def signUp():
    return data.templates["signUp"].render(
        **baseTemplateKwargs
    )


def login():
    return data.templates["login"].render(
        **baseTemplateKwargs
    )