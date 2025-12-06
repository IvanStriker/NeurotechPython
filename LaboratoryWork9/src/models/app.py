from .author import Author


class App:
    def __init__(self, name: str, version: str, author: Author):
        self.name = name
        self.version = version
        self.author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 5 and all(i.isdigit() for i in name):
            raise ValueError(
                f"App.name: invalid name for application {name}"
            )
        self.__name = name

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        if len(version) < 1 and any(not i.isdigit() and i != '.'
                                     for i in version):
            raise ValueError(
                f"App.name: invalid version for application {version}"
            )
        self.__version = version

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: Author):
        self.__author = author