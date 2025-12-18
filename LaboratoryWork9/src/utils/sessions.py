import threading
import time
import uuid
from typing import Any

from .decorators import check_types


class Session:
    """
    Represents a user session.
    """

    def __init__(self):
        """
        Initializes an unauthorized new Session.
        """
        self.__id = str(uuid.uuid4())
        self.__last_access = time.time()
        self.__user_id = -1

    @property
    def id(self) -> str:
        """
        Gives back the session ID and updates last
        access time.

        Returns:
            str: The session id
        """
        self.__last_access = time.time()
        return self.__id

    @property
    def last_access(self) -> float:
        """
        Gets the last access timestamp and updates to current time.

        Returns:
            float: The timestamp of the previous access in
                seconds since epoch.
        """
        res: float = self.__last_access
        self.__last_access = time.time()
        return res

    @property
    def authorized(self) -> bool:
        """
        Checks if the session is authorized.

        Returns:
            bool: True if user_id is not -1, False otherwise.
        """
        return self.__user_id != -1

    @property
    def userID(self) -> int:
        """
        Gets the user ID associated with this session.

        Returns:
            str: The user identifier or -1 if unauthorized.
        """
        return self.__user_id

    @userID.setter
    @check_types(Any, int)
    def userID(self, userID: int) -> None:
        """
        Sets the user ID for this session,
        affecting authorization state.

        Args:
            userID (int): The new user identifier.
                Use -1 to deauthorize.
        """
        self.__user_id = userID


class SessionManager:
    """
    Manages creation, retrieval, and cleanup of Session objects.

    Provides thread-safe session management with automatic
    garbage collection of expired sessions.
    """

    @check_types(Any, float | int)
    def __init__(self, lifetime: float):
        """
        Initializes a SessionManager with specified session lifetime.

        Args:
            lifetime (float | int): Session lifetime in
                seconds before expiry. Auto-cleanup runs
                every 60 seconds.

        Note:
            Starts a background garbage collector thread timer.
        """
        self.__sessions: dict[str, Session] = {}
        self.__lifetime = lifetime
        self.__mutex = threading.Lock()
        self.__garbage_collector = threading.Timer(
            60,
            self.__collectOutdated
        )

    def create(self) -> Session:
        """
        Creates a new session and adds it to the managed sessions.

        Returns:
            Session: A newly created Session object with unique ID.

        Note:
            Thread-safe operation using mutex locking.
        """
        with self.__mutex:
            session = Session()
            self.__sessions[session.id] = session
        return session

    def __collectOutdated(self) -> None:
        """
        Removes sessions that have exceeded their lifetime.

        Compares current time against last_access time for each session.
        Thread-safe operation using mutex locking.
        """
        with self.__mutex:
            currentTime = time.time()
            outdated = [
                i for i, val in self.__sessions.items()
                if currentTime - val.last_access >
                   self.__lifetime
            ]
            for sessionID in outdated:
                self.__sessions.pop(sessionID)

    @check_types(Any, str)
    def get(self, id: str) -> Session:
        """
        Retrieves a session by its ID.

        Args:
            id (str): The session ID to look up.

        Returns:
            Session: The Session object if found, None otherwise.
        """
        return self.__sessions.get(id)

    def __del__(self):
        """
        Cleanup destructor that cancels the garbage collector timer.

        Ensures proper cleanup of background threads when
        manager is destroyed.
        """
        self.__garbage_collector.cancel()