from threading import Thread, Lock
from time import sleep
from random import randint

res = []


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            add_sum = randint(50, 500)
            with self.lock:
                self.balance += add_sum
                dep = f"Пополнение: {add_sum} Баланс: {self.balance} "
                res.append(dep)
                # print(f"Пополнение: {add_sum} Баланс: {self.balance} ")
            sleep(0.001)

    def take(self):
        for i in range(100):
            sub_sum = randint(50, 500)
            request = f"Запрос на снятие {sub_sum}."
            res.append(request)
            # print(f"Запрос на снятие {sub_sum}.")
            with self.lock:
                if sub_sum <= self.balance:
                    self.balance -= sub_sum
                    take = f"Снятие: {sub_sum} Баланс: {self.balance} "
                    res.append(take)
                    # print(f"Снятие: {sub_sum} Баланс: {self.balance} ")
                else:
                    request_deny = "Запрос отклонен, недостаточно средств"
                    res.append(request_deny)
                    # print("Запрос отклонен, недостаточно средств")
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()


for item in res:
    print(item)
print(f"Итоговый баланс: {bk.balance}")


