import datetime as dt

yesterday = dt.date.today() - dt.timedelta(days=1)
day_before_yesterday = dt.date.today() - dt.timedelta(days=2)
today = dt.date.today()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_PARAMETER = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "someapikey",
    "outputsize": "compact"
}

NEWS_PARAMETER = {
    "qInTitle": COMPANY_NAME,
    "from": yesterday,
    "to": today,
    "sortBy": "popularity",
    "apiKey": "someapikey",
    "pageSize": 3
}


