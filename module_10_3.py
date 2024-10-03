from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            add_sum = randint(50, 500)
            self.balance += add_sum
            print(f"Пополнение: {add_sum} Баланс: {self.balance} ")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            sub_sum = randint(50, 500)
            print(f"Запрос на снятие {sub_sum}.")
            if sub_sum <= self.balance:
                self.balance -= sub_sum
                print(f"Снятие: {sub_sum} Баланс: {self.balance} ")
            else:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
