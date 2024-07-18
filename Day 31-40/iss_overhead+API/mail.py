import smtplib


EMAIL = "dummy@gmail.com"
PASSWORD = "notarealpassword"


def sendmail(recipient):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipient,
                            msg=f'Subject:The ISS is Here\n\nLook Up')
