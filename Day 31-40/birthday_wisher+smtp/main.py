from quote_gen import Quote
import datetime as dt
from mail import Mail, sendmail
import random

mail = Mail()
quote = Quote()
now = dt.datetime.now()

birthday_dict = mail.birthday_dict

birthday_check = (now.month, now.day)

if birthday_check in birthday_dict:
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as file:
        birthday_person = birthday_dict[birthday_check]['name']
        content = file.read()
        birthday_txt = content.replace('[NAME]', f'{birthday_person}')

    sendmail(birthday_dict[birthday_check][1], birthday_txt)
