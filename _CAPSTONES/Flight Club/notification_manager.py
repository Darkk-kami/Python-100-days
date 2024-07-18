import smtplib
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.client = Client("twiliousername", "twilioauth")
        self.connection = smtplib.SMTP("emailprovidersmtp")
        self.email = "getyourownemail"
        self.email_password = "getyourownpassword"

    def send_sms(self, message_body):
        self.client.messages.create(
            from_="you@mail.com",
            body=message_body,
            to="whoyoulike@mail.com"
        )

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email[1],
                    msg=f"Subject:New Low Price Flight!\n\nHey {email[1]}!\n{email_body}".encode('utf-8')
                )
