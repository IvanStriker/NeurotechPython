from .base_model import BaseModel

class Currency(BaseModel):
    def __init__(self, id: str, num_code: int,
                 char_code: str, name: str, value: float,
                 nominal: int):
        BaseModel.__init__(self, id)
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, num_code: int):
        self.__num_code = num_code

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, char_code: str):
        if len(char_code) != 3:
            raise ValueError(
                f"Currency.char_code: invalid char_code for currency: "
                f"{char_code}"
            )
        self.__char_code = char_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) == "":
            raise ValueError(
                f"Currency.name: invalid name for currency: "
                f"{name}"
            )
        self.__name = name

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        if value <= 0:
            raise ValueError(
                f"Currency.value: invalid value for currency: "
                f"{value}"
            )
        self.__value = value

    @property
    def nominal(self):
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal: int):
        if nominal <= 0:
            raise ValueError(
                f"Currency.value: invalid nominal for currency: "
                f"{nominal}"
            )
        self.__nominal = nominal

    def parseDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "charCode": self.char_code,
            "value": self.value,
            "nominal": self.nominal,
        }
