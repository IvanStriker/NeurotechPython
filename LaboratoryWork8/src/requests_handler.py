import http.cookies
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
from typing import Callable, Any

import requests.exceptions

import LaboratoryWork8.src.controllers as controllers
import LaboratoryWork8.src.utils.sessions as sessions
from LaboratoryWork8.src.utils.decorators import check_types


urls: dict[str, Callable] = {
    "/": controllers.root,
    "/currencies": controllers.currencies,
    "/currencies/subscribe": controllers.currencies,
    "/users": controllers.users,
    "/user": controllers.profile,
    "/profile": controllers.profile,
    "/signUp": controllers.signUp,
    "/login": controllers.login,
    "/author": controllers.author,
}


sessionManager = sessions.SessionManager(7200)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the currency application.
    """

    def __getSession(self) -> sessions.Session:
        """
        Gives back or creates a session

        Returns:
            sessions.Session: The current or created session object
        """
        cookie = http.cookies.SimpleCookie(self.headers.get('Cookie', ''))
        if "session" in cookie:
            session = sessionManager.get(
                cookie["session"].value
            )
            if session:
                return session
        session = sessionManager.create()
        return session


    @check_types(Any, sessions.Session)
    def __sendCookie(self, session: sessions.Session):
        """
        Sends session cookie to the client

        Args:
            session (sessions.Session): Session object to send
        """
        cookie = http.cookies.SimpleCookie()
        cookie['session'] = session.id
        self.send_header('Set-Cookie', cookie.output(header=''))

    def do_POST(self):
        """
        Handles HTTP POST requests through redirecting to GET handler
        """
        self.do_GET()

    def do_GET(self):
        """
        Prime request handler with routing
        """
        queryPieces: list[str] = self.path.split("?")
        queryParams: dict[str, list[str]]
        try:
            queryParams = parse_qs(queryPieces[1])
        except IndexError:
            queryParams = {}
        address: str = queryPieces[0]
        session = self.__getSession()
        try:
            html = urls[address](queryParams, session)
            self.send_response(200)
            self.send_header("Content-type",
                             "text/html; encoding: utf-8")
            self.__sendCookie(session)
            self.end_headers()
            self.wfile.write(
                bytes(
                    html,
                    encoding="utf-8"
                )
            )
        except (requests.exceptions.RequestException,
                TypeError, ValueError):
            self.send_response(400)
            self.__sendCookie(session)
            self.end_headers()
        except KeyError as e:
            self.send_response(404)
            self.__sendCookie(session)
            self.end_headers()

    # def do_POST(self):
    #     """Alternative POST handler implementation (commented out)."""
    #     if self.path.split("?")[0] not in views:
    #         self.send_response(404)
    #     else:
    #         views[self.path.split("?")[0]](self)