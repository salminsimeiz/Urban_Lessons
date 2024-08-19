
from math import acos
from random import random
import matplotlib.pyplot as plt


def match_stat(m_length: float, gap: float, num: int) -> []:
    """
        Эта функция предназначена для решения одной задачи по статистике:
    между двумя параллельными прямыми бросают спичку, длина которой больше расстояния между прямыми.
    Нужно найти вероятность того,что спичка окажется между прямыми.
        Очевидно,что эта вероятность пропорциональна расстоянию между прямыми и обратно пропорциональ-
    на длине спички. Не решая задачу математическими методами, моделируем этот процесс и находим коэф-
    фициент пропорциональности. Чем больше  проведенных экспериментов, тем точнее получается  значение
    коэффициента ->1. Таким образом, измеряя геометрию  можно узнать вероятность, которая определяется
    только соотношением gap/m_length.

    :param m_length: длина спички
    :param gap: расстояние между параллельными прямыми
    :param num: число экспериментов (бросаний спички)
    """
    (x, y, simulated) = ([], [], [])
    while gap > 0:
        n = 0
        angle_min = acos(gap / m_length)
        for i in range(num):
            angle = acos(random())
            if angle >= angle_min:
                n += 1
        x.append(gap / m_length)
        y.append(n / num)
        gap -= 0.2
    simulated = x
    return x, y, simulated


match_stat(8, 1.5, 1000)
plt.plot(match_stat(8, 1.5, 1000)[0], match_stat(8, 1.5, 1000)[2], color="red")
plt.scatter(match_stat(8, 1.5, 1000)[0], match_stat(8, 1.5, 1000)[1], color="green", marker="o")
match_stat(8, 1.5, 50000)
plt.scatter(match_stat(8, 1.5, 50000)[0], match_stat(8, 1.5, 50000)[1], marker="+")
plt.xlabel("Относительная ширина щели")
plt.ylabel("Вероятность")
plt.title("Зависимость вероятности от геометрии")
plt.show()
