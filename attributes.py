class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание: {self.name}, имеет {self.number_of_floors} этажей! \nЯ поднимаюсь на {new_floor}-й.')
        if new_floor < 1  or new_floor > self.number_of_floors:
            print(f'{new_floor}.. Такого этажа не существует!')
        else:
            for new_floor in range(floor):
                print(floor +1)


dev1 = House("ЖК Эльбрус", 30)
dev2 = House("ЖК Лотан", 17)

dev1.go_to(31)
print("\t")
dev2.go_to(18)