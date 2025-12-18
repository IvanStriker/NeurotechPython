import uuid

from LaboratoryWork9.src.utils import sessions

import LaboratoryWork9.src.views as views
import LaboratoryWork9.src.data as data
import LaboratoryWork9.src.models as models
from LaboratoryWork9.src.utils.decorators import check_types


@check_types(dict, sessions.Session, str)
def getUser(queryParams: dict[str, list[str]],
            session: sessions.Session,
            errorText: str) -> models.User:
    """
    Retrieves a user based on query parameters or session authorization.

    Attempts to get user by ID from queryParams, then falls back to
    session's authorized user. Raises error if neither is available.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
        session (sessions.Session): Current user session.
        errorText (str): Error message prefix for authorization
            failures.

    Returns:
        models.User: The requested or session-authorized User object.

    Raises:
        ValueError: If no ID provided in queryParams and
            session is not authorized.
    """
    if "id" in queryParams:
        return data.users.get(int(queryParams["id"][0]))
    if session.authorized:
        return data.users.get(session.userID)
    raise ValueError(
        f"{errorText}: You haven't been authorized."
    )


@check_types(dict, sessions.Session)
def root(queryParams: dict[str, list[str]],
         session: sessions.Session):
    """
    Handles the root/main page request.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
        session (sessions.Session): Current user session.

    Returns:
        Rendered root page view.
    """
    return views.root()


@check_types(dict, sessions.Session)
def currencies(queryParams: dict[str, list[str]],
               session: sessions.Session):
    """
    Handles currencies page and subscription management.

    If queryParams contains 'id', adds currency subscription
        for current user. Otherwise, loads currency data.
        Thread-safe for subscription operations.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
            'id' key triggers subscription.
        session (sessions.Session): Current user session
            for authorization.

    Returns:
        Rendered currencies page view.
    """
    if queryParams:
        user = getUser({}, session, "Currencies page")
        data.addSubscription(
            models.UserCurrency(
                0, user.id, int(queryParams["id"][0])
            )
        )
    return views.currencies(data.currencies.getAll())


@check_types(dict, sessions.Session)
def profile(queryParams: dict[str, list[str]],
            session: sessions.Session):
    """
    Handles user profile page requests.

    Retrieves user based on queryParams or session,
    renders profile view.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters
            may contain 'id' for specific user.
        session (sessions.Session): Current user
            session for fallback.

    Returns:
        Rendered profile page view for the requested user.
    """
    user = getUser(queryParams, session,
                   "Profile page controller")
    return views.profile(user, data.currencies.getForUser(user.id))


@check_types(dict, sessions.Session)
def users(queryParams: dict[str, list[str]],
          session: sessions.Session):
    """
    Handles users listing page.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
        session (sessions.Session): Current user session.

    Returns:
        Rendered users listing page view.
    """
    return views.users(data.users.getAll())


@check_types(dict, sessions.Session)
def signUp(queryParams: dict[str, list[str]],
           session: sessions.Session):
    """
    Handles user registration (sign-up) process.

    If queryParams contains registration data, creates new user,
    sets session, and redirects to profile.
    Otherwise shows registration form.

    Args:
        queryParams (dict[str, list[str]]): Registration form
            data with 'firstName' and 'lastName'.
        session (sessions.Session): Current user session
            for authorization.

    Returns:
        Registration form or new user profile.
    """
    if queryParams:
        user = models.User(0,
                           queryParams["firstName"][0] + " " +
                           queryParams["lastName"][0])
        data.addUser(user)
        session.userID = user.id
        return profile(queryParams, session)

    return views.signUp()


@check_types(dict, sessions.Session)
def login(queryParams: dict[str, list[str]],
          session: sessions.Session):
    """
    Handles user login authentication.

    If queryParams contains credentials, authenticates
    user by name match, sets session, and redirects to profile.
    Otherwise shows login form.

    Args:
        queryParams (dict[str, list[str]]): Login form data with
            'firstName' and 'lastName'.
        session (sessions.Session): Current user session
            for authorization.

    Returns:
        Login form or authenticated profile.
    """
    if queryParams:
        name = (queryParams["firstName"][0] + " " +
                queryParams["lastName"][0])
        user = data.users.getByName(name)
        session.userID = user.id
        return profile(queryParams, session)

    return views.login()


@check_types(dict, sessions.Session)
def author(queryParams: dict[str, list[str]],
           session: sessions.Session):
    """
    Handles author information page.

    Args:
        queryParams (dict[str, list[str]]): URL query parameters.
        session (sessions.Session): Current user session.

    Returns:
        Rendered author information page view.
    """
    return views.author()
