import requests
from parameters import STOCK_PARAMETER, NEWS_PARAMETER, today, yesterday, day_before_yesterday
from twilio.rest import Client
import os

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
API_KEY = os.environ.get("API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

is_up = True
stock_sym = None


def change(closing, opening):
    global is_up
    difference = closing - opening
    percentage = (difference/opening) * 100
    is_up = percentage > 0
    return abs(percentage)


news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETER).json()["articles"]
stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETER).json()["Time Series (Daily)"]

stock_price = stock_response[f"{day_before_yesterday}"]

change_in_stock = change(closing=float(stock_price["4. close"]), opening=float(stock_price["1. open"]))

if change_in_stock > 1:
    if is_up:
        stock_sym = "🔺"
    else:
        stock_sym = "🔻"
    client = Client(account_sid, auth_token)
    article = [(f'TSLA:{stock_sym}{change_in_stock}%\nHeadline: {news["title"]}\nBrief: '
                f'{news["description"]}\nUrl:{news["url"]}') for news in news_response]

    for news in article:
        message = client.messages.create(
            body=article,
            from_=os.environ.get("A_NUMBER"),
            to=os.environ.get("P_NUMBER"),
        )
