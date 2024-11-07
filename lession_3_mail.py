import os
import smtplib


from dotenv import load_dotenv
load_dotenv()
key = os.getenv("MY_KEY")
login = os.getenv("MY_LOGIN")


site_name = """https://dvmn.org/referrals/7uSIJekEqtbonhyR23wpLVOWM4KeIzZRFNyMYUiW/"""
friend_name = "Владислав"
sender_name = """Сергей"""
sender_email = login
recipient_email = "pythontestt@yandex.ru"
subject_email = "Приглашение"

letter_template = """\
From: {sender_e}
To: {recipient_e}
Subject: {subject_e}
Content-Type: text/plain; charset="UTF-8";
 
 
 Привет, {f_n}! {m_n} приглашает тебя на сайт {ws}!

{ws} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на {ws}?

 Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {ws}
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл. """.format(sender_e = sender_email,
recipient_e = recipient_email, subject_e = subject_email, f_n = friend_name , m_n = sender_name, ws = site_name)
letter = letter_template
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(login, key)
server.sendmail(sender_email, recipient_email, letter)
server.quit()

