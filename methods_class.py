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
