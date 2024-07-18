import requests
from bs4 import BeautifulSoup
from smtplib import SMTP_SSL
from email.message import EmailMessage
import os
import dotenv

dotenv.load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 100
HOST = "smtp.gmail.com"
PORT = 465

soup = BeautifulSoup(requests.get(URL, headers={"Accept-Language": "en-NG,en-US;q=0.9,en-GB;q=0.8,en;q=0.7",
                                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                                                              "Safari/537.36"
                                                }).text, "html.parser")


price = float(soup.find(class_="a-offscreen").text.strip("$"))
print(price)

if price < TARGET_PRICE:
    with SMTP_SSL(HOST, port=PORT) as server:
        email = EmailMessage()
        email["Subject"] = "Price Drop Alert!!!"
        email["From"] = os.getenv("SENDER_EMAIL")
        email["To"] = os.getenv("SENDER_EMAIL")
        email.set_content(f"The pot is now at ${price}.\n{URL}")

        server.login(user=os.getenv("SENDER_EMAIL"), password=os.getenv("EMAIL_PASSWORD"))
        server.send_message(email)

