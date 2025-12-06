class BaseModel:
    def __init__(self, id: str):
        self.id = id

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id