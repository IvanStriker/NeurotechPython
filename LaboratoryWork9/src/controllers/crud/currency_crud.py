from .base_crud import BaseCRUD
from ...models import Currency


class CurrencyCRUD(BaseCRUD):
    def __init__(self):
        BaseCRUD.__init__(
            self,
            "currencies",
            (
                ("num_code", "TEXT NOT NULL", str),
                ("char_code", "TEXT NOT NULL", str),
                ("name", "TEXT NOT NULL", str),
                ("value", "FLOAT", float),
                ("nominal", "INTEGER", int)
            ),
            Currency
        )