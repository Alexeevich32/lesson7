class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'{self.name}, имеет {self.number_of_floors} этажей! \nЯ поднимаюсь на {new_floor}-й.')
        if new_floor < 1  or new_floor > self.number_of_floors:
            print(f'{new_floor}.. Такого этажа не существует!')
        else:
            for new_floor in range(floor):
                print(floor +1)



    def __len__(self):
        return self.number_of_floors

    def __str__(self):
       return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    def __eq__(self, other):
        return self.name == other.name and self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self


    def __iadd__(self, value):
        if isinstance(value, int):
           return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)





dev1 = House("ЖК Эльбрус", 30)
dev2 = House("ЖК Лотан", 17)
print(dev1)
print(dev2)
print(len(dev1))
print(len(dev2))
print("\t")

dev1.go_to(3)
print("\t")
dev2.go_to(8)

dev2.name = 'ЖК Эльбрус'
print(dev1 == dev2)  # __eq__

print(dev1 < dev2)  # __lt__

print(dev1 <= dev2)  # __le__

print(dev1 > dev2)   # __gt__

print(dev1 >= dev2)   # __ge__

print(dev1 != dev2)    # __ne__

dev1 = dev1 + 10
print(dev1)    # __add__

dev1 += 10
print(dev1)  # __iadd__

dev2 = 10 + dev2
print(dev2)     # __radd__
