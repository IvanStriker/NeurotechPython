from .base_crud import BaseCRUD
from LaboratoryWork9.src.models.user import User


class UserCRUD(BaseCRUD):
    """
    BaseCRUD instance for User ops
    """
    def __init__(self):
        """
        Initializes BaseCRUD with user-specific schema
        """
        BaseCRUD.__init__(
            self,
            "users",
            (
                ("name", "TEXT NOT NULL", str),
            ),
            User
        )