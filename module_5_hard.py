from time import sleep


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname}, {self.age}"

 
# Проверка сложности паролей
def password_check(word: str):
    if len(word) < 8 or word.islower() or word.isalpha():
        print("Придумайте более сложный пароль")
        return False
    else:
        return True


def reg():
    (n, p, a) = (0, 0, 0)
    fl_ag = True
    while fl_ag is True:
        n = input("Введите логин: ")
        p = input("Введите пароль: ")
        if password_check(p) is True:
            p1 = input("Повторите пароль: ")
            a = int(input("Введите Ваш возраст: "))
            if p == p1:
                fl_ag = False
            else:
                print("Пароли не совпадают - повторите ввод")
                fl_ag = True
    return User(n, p, a)


def log():
    (n, p, a) = (0, 0, 0)
    flag_ = True
    while flag_ is True:
        n = input("Введите логин: ")
        p = input("Введите пароль: ")
        if password_check(p) is True:
            p1 = input("Повторите пароль: ")
            a = int(input("Введите Ваш возраст: "))
            if p == p1:
                flag_ = False
            else:
                print("Пароли не совпадают - повторите ввод")
                flag_ = True
    return User(n, p, a)


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        if self.adult_mode is False:
            return f"{self.title}, 18+"
        else:
            return f"{self.title}, 0+"


class UrTube:
    users = []
    videos = []
    def __init__(self):
        self.current_user = None

    def log_in(self):
        n = input("Введите логин: ")
        p = input("Введите пароль: ")
        for item in self.users:
            if item.nickname == n and item.password == hash(p):
                self.current_user = item
                break
        else:
            print("Пароль/Логин введены неправильно.")
            sleep(2)
            print("По-видимому, Вы забыли пароль - зарегистрируйтесь заново")
            exit()

    def log_out(self):
        self.current_user = None

    def register(self):
        u = reg()
        for item in self.users:
            if u.nickname == item.nickname:
                print(f"Пользователь {u.nickname} уже существует, зарегистрируйтесь заново")
                break
        else:
            self.users.append(u)

    def add(self):
        print("Вход для администратора")
        name = input("name? (admin) ")
        if name == "admin":  # логин "admin"
            fl = True
            while fl is True:
                t_tle = input("title? ")
                dur_n = int(input("duration? "))
                time_n = 0
                ad_mode = bool(int(input("0+:? (0/1) ")))
                film = Video(t_tle, dur_n, time_n, ad_mode)
                for item in self.videos:
                    if item.title == film.title:
                        break
                else:
                    self.videos.append(film)
                q = input("Продолжить ввод фильмов?(y/n) ")
                if q == "y":
                    fl = True
                else:
                    fl = False
            print("СПИСОК ФИЛЬМОВ:")
            for item in self.videos:
                print(item)
        else:
            exit()

    def get_video(self, w_d: str) -> list:
        film_lst = []
        for item in self.videos:
            if w_d.lower() in item.title.lower():
                film_lst.append(item.title)
        return film_lst

    def watch_video(self):
        film_title = input("Для просмотра введите название фильма: ")
        for item in self.videos:
            if film_title == item.title:
                if (ur.current_user.age > 18 and item.adult_mode is False) or item.adult_mode is True:
                    for t in range(item.duration + 1):
                        item.time_now = t
                        print(t, end=" ")
                        sleep(1)
                    print("Конец видео")
                    item.time_now = 0
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    item.time_now = 0


if __name__ == "__main__":
    ur = UrTube()
    ur.add()    # нужно сохранить список фильмов в файл или БД, но пока - нет
# прямой вход в сервис не реализован, поскольку не сохранена база юзеров в файле
    hello = input("Здравствуйте, Вы хотите зарегистрироваться (1) или войти в сервис(2)? ")
    if int(hello) == 1:
        while True:
            if input("Хотите зарегистрироваться? (y/n) ") == "y":
                ur.register()
            else:
                break
        print("Войдите в сервис")
        ur.log_in()
        while True:
            word = input("Введите слово для поиска фильма: ")
            ur.get_video(word)
            print(ur.get_video(word))
            ur.watch_video()
            ex = input("Хотите выйти из сервиса?(y/n) ")
            if ex == "y":
                ur.log_out()
                print(ur.current_user)
                break 
        exit()
    elif int(hello) == 2:
        ur.log_in()
        word = input("Введите слово для поиска фильма: ")
        ur.get_video(word)
        print(ur.get_video(word))
        ur.watch_video()
        ur.log_out()
    else:
        exit()
