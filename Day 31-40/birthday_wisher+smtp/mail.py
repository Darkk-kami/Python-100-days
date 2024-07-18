import smtplib
import pandas
import random

EMAIL = "dummy@gmail.com"
PASSWORD = "notarealpassword"


def sendmail(recipient, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipient,
                            msg=f'Subject:Happy Birthday\n\n{message}')


class Mail:
    def __init__(self):
        data = pandas.read_csv('birthdays.csv')
        self.birthday_dict = {(row['month'], row['day']): row for index, row in data.iterrows()}






