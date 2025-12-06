class Human:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name == "":
            raise ValueError(
                f"{self.__class__}.name: invalid name for "
                f"{self.__class__} {name}"
            )
        self.__name = name
