from threading import Thread
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number: int):
        self.number = number
        self. guest = None


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    guest.start()
                    print(f"{guest.name} сел(села) за стол номер {table.number}")
                    guest.join()
                    break
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None and Guest(table.guest).is_alive() is False:
                    print(f"{Guest(table.guest).name} покушал(а) и ушел(ушла)")
                    print(f"Стол {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        guest_next = self.queue.get()
                        table.guest = guest_next.name
                        print(f"{table.guest} вышел(вышла) из очереди и сел(села) за стол номер {table.number}")
                        guest_next.start()
                        guest_next.join()


tables = [Table(number) for number in range(1, 6)]
guests_names = [
  'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
  'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
