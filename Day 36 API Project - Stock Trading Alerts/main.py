import os
import smtplib
from datetime import date, timedelta
import requests

STOCK_NAME = "INTC"
COMPANY_NAME = "Intel Corp"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR_API_KEY_HERE"
NEWS_API_KEY = "YOUR_API_KEY_HERE"

STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    # "country": "us",
    "apiKey": NEWS_API_KEY,
}

## _-_-_-_-_- STOCK API CALL -_-_-_-_-_ ##
response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
response.raise_for_status()
stock_data = response.json()

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)

yesterday_closing_price = stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"]
day_before_yesterday_closing_price = stock_data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"]

closing_price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
percentage_difference = (float(closing_price_difference) / float(day_before_yesterday_closing_price)) * 100

if percentage_difference >= 0.5:
    ## _-_-_-_-_- NEWS API CALL -_-_-_-_-_ ##
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    response.raise_for_status()
    news_data = response.json()
    news_list_comp = [
        {"headline": article["title"], "description": article["description"]}
        for article in news_data['articles'][:3]
    ]

    for item in news_list_comp:
        title = item['headline'].encode('utf-8')
        description = item['description'].encode('utf-8')
        python_email = os.getenv('PYTHON_EMAIL')
        app_password = os.getenv("APP_PASSWORD")

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=python_email, password=app_password)
            connection.sendmail(
                from_addr=python_email,
                to_addrs=python_email,
                msg=f"{title}\n\n{description}",)

