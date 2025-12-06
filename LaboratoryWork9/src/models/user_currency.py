from .base_model import BaseModel


class UserCurrency(BaseModel):
    def __init__(self, id: str, user_id: str, currency_id: str):
        BaseModel.__init__(self, id)
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def currency_id(self):
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, currency_id: str):
        self.__currency_id = currency_id