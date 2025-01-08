def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    valid_domain = ['.com', '.ru', '.net']

    valid_sender = False
    for domain in valid_domain:
        if sender.endswith(domain):
            valid_sender = True
        if '@' not in sender:
            valid_sender = False
            break

    valid_recipient = False
    for domain in valid_domain:
        if recipient.endswith(domain):
            valid_recipient = True
        if '@' not in recipient:
            valid_recipient = False
            break

    if not valid_sender or not valid_recipient:
        print('Невозможно отправить письмо с адреса:', sender, 'на адрес:',recipient )
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес:', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес:', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
