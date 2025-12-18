from .base_crud import BaseCRUD
from LaboratoryWork9.src.models.user import User


class UserCRUD(BaseCRUD):
    def __init__(self):
        BaseCRUD.__init__(
            self,
            "users",
            (
                ("name", "TEXT NOT NULL", str),
            ),
            User
        )