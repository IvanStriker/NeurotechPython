from .human import Human
from .base_model import BaseModel


class User(BaseModel, Human):
    def __init__(self, id: str, name: str):
        Human.__init__(self, name)
        BaseModel.__init__(self, id)
