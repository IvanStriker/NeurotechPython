import http.server
import threading
import unittest
import uuid

import requests

from LaboratoryWork8.src import models
from LaboratoryWork8.src.utils import get_currencies
import LaboratoryWork8.src.data as data
from LaboratoryWork8.src.views import baseTemplateKwargs
import LaboratoryWork8.src.views as views
from LaboratoryWork8.src.requests_handler import SimpleHTTPRequestHandler


class TestModels(unittest.TestCase):
    def testAuthor(self):
        with self.assertRaises(ValueError):
            models.Author("Ivan", "03121")
        author = models.Author("Ivan", "P3121")
        self.assertEqual(author.name, "Ivan")
        self.assertEqual(author.group, "P3121")

        with self.assertRaises(ValueError):
            author.name = "-"
        with self.assertRaises(ValueError):
            author.group = "0"

    def testApp(self):
        with self.assertRaises(ValueError):
            models.App("Mine", "1-2",
                       models.Author("Ivan", "P3121"))
        app = models.App("My App", "1.2",
                         models.Author("Ivan", "P3121"))
        self.assertEqual(app.name, "My App")
        self.assertEqual(app.version, "1.2")
        self.assertEqual(app.author.name, "Ivan")
        self.assertEqual(app.author.group, "P3121")

        with self.assertRaises(ValueError):
            app.name = "1"
        with self.assertRaises(ValueError):
            app.version = "HA!!"
        with self.assertRaises(ValueError):
            app.author.group = "112333"

    def testUser(self):
        with self.assertRaises(ValueError):
            models.User(str(uuid.uuid4()), "-")
        id = str(uuid.uuid4())
        user = models.User(id, "Ivan")
        self.assertEqual(user.name, "Ivan")
        self.assertEqual(user.id, id)

        with self.assertRaises(ValueError):
            user.name = "-"

    def testCurrency(self):
        with self.assertRaises(ValueError):
            models.Currency(str(uuid.uuid4()), 5,
                            "#", "Dollar", 100, 1)
        id = str(uuid.uuid4())
        currency = models.Currency(id, 50,
                                   "USD", "Dollar",
                                   100, 1)
        self.assertEqual(currency.id, id)
        self.assertEqual(currency.char_code, "USD")
        self.assertEqual(currency.num_code, 50)
        self.assertEqual(currency.name, "Dollar")
        self.assertEqual(currency.value, 100)
        self.assertEqual(currency.nominal, 1)

        with self.assertRaises(ValueError):
            currency.name = ""
        with self.assertRaises(ValueError):
            currency.char_code = "A"
        with self.assertRaises(TypeError):
            currency.num_code = "5"
        with self.assertRaises(ValueError):
            currency.value = -6
        with self.assertRaises(ValueError):
            currency.nominal = 0

    def testUserCurrency(self):
        with self.assertRaises(TypeError):
            models.UserCurrency(str(uuid.uuid4()), "0", 7)
        id = str(uuid.uuid4())
        user_currency = models.UserCurrency(id, "0", "1")
        self.assertEqual(user_currency.id, id)
        self.assertEqual(user_currency.user_id, "0")
        self.assertEqual(user_currency.currency_id, "1")


class TestCurrenciesApi(unittest.TestCase):
    def testBasic(self):
        lst = ['AUD', 'AZN', 'DZD']
        curs = get_currencies(lst)
        for item in curs.values():
            self.assertTrue(isinstance(item, models.Currency))
            self.assertIn(item.char_code, lst)

    def testRaises(self):
        with self.assertRaises(
                requests.exceptions.ConnectionError):
            get_currencies(url="http://")

        with self.assertRaises(KeyError):
            get_currencies(["You won't find!"])


class TestServer(unittest.TestCase):
    def setUp(self):
        data.load_data()
        self.__mutex = threading.Lock()
        self.__server = http.server.HTTPServer(
            ("localhost", 8080),
            SimpleHTTPRequestHandler
        )
        self.__thread = threading.Thread(
            target=self.__server.serve_forever
        )
        self.__thread.start()

    def testIndex(self):
        response = requests.get("http://localhost:8080/")
        response.raise_for_status()
        self.assertEqual(
            response.content,
            bytes(views.root(), encoding="utf-8")
        )

    def testUser(self):
        response = requests.get("http://localhost:8080/user?id=0")
        response.raise_for_status()
        self.assertEqual(
            response.content,
            bytes(views.profile(data.users["0"]), encoding="utf-8")
        )

    def testUsers(self):
        response = requests.get("http://localhost:8080/users")
        response.raise_for_status()
        self.assertEqual(
            response.content,
            bytes(views.users(), encoding="utf-8")
        )

    def testCurrencies(self):
        response = requests.get("http://localhost:8080/currencies")
        response.raise_for_status()
        self.assertEqual(
            response.content,
            bytes(views.currencies(), encoding="utf-8")
        )

    def testAuthor(self):
        response = requests.get("http://localhost:8080/author")
        response.raise_for_status()
        self.assertEqual(
            response.content,
            bytes(views.author(), encoding="utf-8")
        )

    def testSignUp(self):
        response = requests.get("http://localhost:8080/signUp?firstName=Ivan&lastName=Kazakov")
        response.raise_for_status()
        response = requests.get("http://localhost:8080/login?firstName=Ivan&lastName=Kazakov")
        response.raise_for_status()
        self.assertEqual(
            response.content,
            bytes(views.profile(
                [val for key, val in
                 data.users.items() if key!="0"][0]
            ), encoding="utf-8")
        )

    def tearDown(self):
        with self.__mutex:
            self.__server.shutdown()
            self.__server.server_close()
        self.__thread.join()


class TestTemplates(unittest.TestCase):
    def setUp(self):
        data.load_templates()

    def testIndex(self):
        html = data.templates["index"].render(
            **baseTemplateKwargs
        )
        self.assertIn(data.app.name, html)
        self.assertIn(data.author.name, html)
        self.assertIn(data.author.group, html)

    def testBase(self):
        html = data.templates["index"].render(
            **baseTemplateKwargs
        )
        for item in baseTemplateKwargs["navigation"]:
            self.assertIn(item["caption"], html)


unittest.main(verbosity=1)