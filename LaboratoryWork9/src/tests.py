import unittest
from unittest.mock import MagicMock

import LaboratoryWork9.src.controllers as ctrs
from LaboratoryWork9.src.models import Currency, UserCurrency, User


class TestControllers(unittest.TestCase):
    def testCurrencyGetAll(self):
        """
        Tests the getAll method of CurrencyController.

        Verifies that:
        1. The controller correctly retrieves all currencies from the database
        2. The returned currency objects have the expected attributes
        3. The database readAll method is called
        """
        mock_db = MagicMock()
        mock_db.readAll.return_value = [
            Currency(**{
                "id": 1,
                "char_code": "USD",
                "value": 90,
                "num_code": "1010",
                "nominal": 1,
                "name": "USA"
            })
        ]
        controller = ctrs.currency_controller.CurrencyController(
            mock_db
        )
        result = controller.getAll()
        self.assertEqual(result[0].char_code, "USD")
        mock_db.readAll.assert_called()

    def testCurrencyGet(self):
        """
        Tests the get method of CurrencyController.
        """
        mock_db = MagicMock()
        mock_db.read.return_value = Currency(**{
            "id": 1,
            "char_code": "USD",
            "value": 90,
            "num_code": "1010",
            "nominal": 1,
            "name": "USA"
        })

        controller = ctrs.currency_controller.CurrencyController(
            mock_db
        )
        result = controller.get(1)
        self.assertEqual(result.char_code, "USD")
        mock_db.read.assert_called()

    def testCurrencySubscribe(self):
        """
        Tests the subscribe method of CurrencyController.
        """
        mock_db = MagicMock()
        db = []
        mock_db.create.side_effect = lambda subscr: db.append(
            subscr.parseDict()
        )

        controller = ctrs.currency_controller.CurrencyController(
            subscriptionCRUD=mock_db
        )
        controller.subscribe(UserCurrency(1, 1, 1))
        self.assertIn(UserCurrency(1, 1, 1).parseDict(), db)
        mock_db.create.assert_called_once()

    def testCurrencyUpdate(self):
        """
        Tests the updateCurrency method of CurrencyController.
        """
        mock_db = MagicMock()

        mock_db.update.return_value = Currency(1, "50", "USD",
                                               "Dollar", 100, 1)

        controller = ctrs.currency_controller.CurrencyController(
            currencyCRUD=mock_db
        )
        result = controller.updateCurrency("USD", 100)
        self.assertAlmostEqual(result.value, 100.0)
        mock_db.update.assert_called_once()

    def testCurrencyDelete(self):
        """
        Tests the deleteCurrency method of CurrencyController.
        """
        mock_db = MagicMock()
        mock_db.read.return_value = Currency(1, "50", "USD",
                                             "Dollar", 100, 1)
        mock_db.delete.return_value = None

        controller = ctrs.currency_controller.CurrencyController(
            currencyCRUD=mock_db
        )
        result = controller.deleteCurrency(1)
        self.assertAlmostEqual(result.value, 100.0)
        mock_db.read.assert_called_once()
        mock_db.delete.assert_called_once()

    def testCurrencyGetForUser(self):
        """
        Tests the getForUser method of CurrencyController.
        """
        mock_db = MagicMock()
        scratch = {
            "num_code": "1010",
            "nominal": 1,
            "name": "USA"
        }
        mock_db.readAll.return_value = [
            Currency(**{"id": 1,
                        "char_code": "USD",
                        "value": 90}
                       | scratch),
            Currency(**{"id": 2,
                        "char_code": "EUR",
                        "value": 100}
                       | scratch)
        ]
        mock_dbs = MagicMock()
        mock_dbs.readAll.return_value = [
            UserCurrency(**{"id": 1, "user_id": 1,
                            "currency_id": 1}),
            UserCurrency(**{"id": 2, "user_id": 1,
                            "currency_id": 2})
        ]
        controller = ctrs.currency_controller.CurrencyController(
            mock_db, mock_dbs
        )
        result = controller.getForUser(1)
        self.assertEqual(len(result), 2)
        mock_db.readAll.assert_called_once()
        mock_dbs.readAll.assert_called_once()

    def testUserGet(self):
        """
        Tests the get and getByName methods of UserController.
        """
        mock_db = MagicMock()
        users = [
            User(**{"id": 1, "name": "Ivan"}),
            User(**{"id": 2, "name": "Artyom"}),
            User(**{"id": 3, "name": "Yaroslav"})
        ]
        mock_db.read.side_effect = lambda attr, val: users[val - 1] \
            if isinstance(val, int) \
            else [i for i in users if i.name == val][0]
        controller = ctrs.user_controller.UserController(
            mock_db
        )
        result = controller.get(1)
        self.assertEqual(result.name, "Ivan")
        self.assertEqual(result.id, 1)
        result = controller.getByName("Ivan")
        self.assertEqual(result.name, "Ivan")
        self.assertEqual(result.id, 1)
        mock_db.read.assert_called()

    def testUserGetAll(self):
        """
        Tests the getAll method of UserController.
        """
        mock_db = MagicMock()
        mock_db.readAll.return_value = [
            User(**{"id": 1, "name": "Ivan"}),
            User(**{"id": 2, "name": "Artyom"}),
            User(**{"id": 3, "name": "Yaroslav"})
        ]
        controller = ctrs.user_controller.UserController(
            mock_db
        )
        result = controller.getAll()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].name, "Ivan")
        mock_db.readAll.assert_called_once()

    def testUserAdd(self):
        """
        Tests the add method of UserController.
        """
        mock_db = MagicMock()
        users = []
        mock_db.create.side_effect = users.append
        controller = ctrs.user_controller.UserController(
            mock_db
        )
        controller.add(User(1, "Ivan"))
        controller.add(User(2, "Sasha"))
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].parseDict(), {"id": 1, "name": "Ivan"})
        self.assertEqual(users[1].parseDict(), {"id": 2, "name": "Sasha"})
        mock_db.create.assert_called()


unittest.main(verbosity=2)