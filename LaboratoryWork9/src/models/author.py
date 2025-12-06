from .human import Human

class Author(Human):
    def __init__(self, name: str, group: str):
        Human.__init__(self, name)
        self.group = group

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        if len(group) < 5 or not (ord('A') <= ord(group[0]) <= ord('Z')):
            raise ValueError(
                f"Author.group: invalid group for author: {group}"
            )
        self.__group = group