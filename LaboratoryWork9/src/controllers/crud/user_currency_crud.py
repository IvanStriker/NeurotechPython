from .base_crud import BaseCRUD
from LaboratoryWork9.src.models import *


class UserCurrencyCRUD(BaseCRUD):
    def __init__(self):
        BaseCRUD.__init__(
            self,
            "subscriptions",
            (
                ("user_id", "INTEGER NOT NULL", int),
                ("currency_id", "INTEGER NOT NULL", int)
            ),
            UserCurrency
        )

    def _create_table(self):
        self._cursor.execute(
            f"""
            CREATE TABLE {self._table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                currency_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES user(id),
                FOREIGN KEY(currency_id) REFERENCES currency(id)
            );
            """
        )