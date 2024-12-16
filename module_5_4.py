class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(*[cls.houses_history])
        return super().__new__(cls)

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __del__(self):
        print(self.name, 'снесен, но остается в истории.')



dev1 = House('ЖК Самолет', 17)
dev2 = House('ЖК Лотан', 25)
dev3 = House('ЖК Эталон', 32)

del dev2
del dev3

print(House.houses_history)







