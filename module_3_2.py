def send_email(message: str, recipient: str, *, sender="university.help@gmail.com"):
    zone = ["com", "ru", "net"]
    try:
        # Обработка шаблона e-mail
        recipient.split("@")[1]
        sender.split("@")[1]
        if recipient.split(".")[-1] not in zone:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        elif sender.split(".")[-1] not in zone:
                    print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    except:
        print("Некорректный шаблон e-mail")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.org')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmailcom')
