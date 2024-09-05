class Vehicle:
    __COLOUR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __colour: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__colour = __colour
        self.__engine_power = __engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__colour}"

    def print_info(self):
        print(Vehicle.get_model(self), Vehicle.get_horsepower(self), Vehicle.get_color(self),
              f"Владелец: {self.owner}", sep="\n", end="\n")

    def set_colour(self, new_colour: str):
        for item in self.__COLOUR_VARIANTS:
            if new_colour.lower() == item.lower():
                self.__colour = new_colour
                break
        else:
            print(f"Нельзя сменить цвет на {new_colour}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_colour('Pink')
vehicle1.set_colour('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
