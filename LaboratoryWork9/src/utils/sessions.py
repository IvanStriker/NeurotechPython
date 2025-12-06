import threading
import time
import uuid
from typing import Any, Callable


class Session:
    def __init__(self):
        self.__id = str(uuid.uuid4())
        self.__last_access = time.time()
        self.__user_id = "-1"

    @property
    def id(self) -> str:
        self.__last_access = time.time()
        return self.__id

    @property
    def last_access(self) -> float:
        res: float = self.__last_access
        self.__last_access = time.time()
        return res

    @property
    def authorized(self) -> bool:
        return self.__user_id != "-1"

    @property
    def userID(self) -> str:
        return self.__user_id

    @userID.setter
    def userID(self, userID: str):
        self.__user_id = userID

class SessionManager:
    def __init__(self, lifetime: float):
        self.__sessions: dict[str, Session] = {}
        self.__lifetime = lifetime
        self.__mutex = threading.Lock()
        self.__garbage_collector = threading.Timer(
            60,
            self.__collectOutdated
        )

    def create(self):
        with self.__mutex:
            session = Session()
            self.__sessions[session.id] = session
        return session

    def __collectOutdated(self):
        with self.__mutex:
            currentTime = time.time()
            outdated = [
                i for i, val in self.__sessions.items()
                if currentTime - val.last_access >
                   self.__lifetime
            ]
            for sessionID in outdated:
                self.__sessions.pop(sessionID)

    def get(self, id: str) -> Session:
        return self.__sessions.get(id)

    def __del__(self):
        self.__garbage_collector.cancel()
