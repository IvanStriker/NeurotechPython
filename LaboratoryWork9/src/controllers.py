import uuid

from utils import sessions

import views
import data
import models


def getUser(queryParams: dict[str, list[str]],
            session: sessions.Session,
            errorText: str) -> models.User:
    if "id" in queryParams:
        return data.users[queryParams["id"][0]]
    if session.authorized:
        return data.users[session.userID]
    raise ValueError(
        f"{errorText}: You haven't been authorized."
    )


def root(queryParams: dict[str, list[str]],
         session: sessions.Session):
    return views.root()


def currencies(queryParams: dict[str, list[str]],
               session: sessions.Session):
    if queryParams:
        user = getUser({}, session, "Currencies page")
        data.addSubscription(
            models.UserCurrency(
                str(uuid.uuid4()), user.id, queryParams["id"][0]
            )
        )
    else:
        data.load_currencies()
    return views.currencies()


def profile(queryParams: dict[str, list[str]],
            session: sessions.Session):
    return views.profile(getUser(queryParams, session,
                                 "Profile page controller"))


def users(queryParams: dict[str, list[str]],
          session: sessions.Session):
    return views.users()


def signUp(queryParams: dict[str, list[str]],
           session: sessions.Session):
    if queryParams:
        user = models.User(str(uuid.uuid4()),
                           queryParams["firstName"][0] + " " +
                           queryParams["lastName"][0])
        data.addUser(user)
        session.userID = user.id
        return views.profile(user)

    return views.signUp()


def login(queryParams: dict[str, list[str]],
          session: sessions.Session):
    if queryParams:
        user = [val for key, val in data.users.items()
                if val.name == queryParams["firstName"][0] + " " +
                queryParams["lastName"][0]][0]
        session.userID = user.id
        return views.profile(user)

    return views.login()
