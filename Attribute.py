class Attribute:
    name = ""

    def __init__(self,name):
        self.name = name

    @property
    def getName(self):
        return self.name

    @name.setter
    def setName(self,name):
        self.name = name


