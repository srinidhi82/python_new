class Myclass:
    def __init__(self, value):
        self.value = value
        self.__variable = 10
        self.name = 'JONNY'


obj = Myclass(10)
#obj.__variable
name = obj.name
print(name)