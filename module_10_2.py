from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.day = 0
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.enemies -= self.power
            self.day += 1
            sleep(1)
            print(f"{self.name} сражается {self.day} день... Осталось {self.enemies} воинов")
        print(f"{self.name} одержал победу спустя {self.day} дней")


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
sleep(1.1)
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
