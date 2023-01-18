"""

"""

# Final Project
# Create an App where it will send you SMS messages when there's a import news from a stock that you have

import requests
import json
from twilio.rest import Client

# API KEYS
STOCK_API_KEY = ""  # --> Personal www.alphavantage.co API KEY
NEWS_API_KEY = ""   # --> Personal https://newsapi.org/ API KEY
twilio_sid_code = ''  # --> Personal Twilio SID
twilio_auth_code = ''   # --> Personal Twilio API KEY

# STOCK = "GOOGL"
# COMPANY_NAME = "Google LLC"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Creating a connection with the Stock API
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
s_data = requests.get("https://www.alphavantage.co/query", params=parameters)
s_data.raise_for_status()
s_json = s_data.json()["Time Series (Daily)"]
s_data_list = [value for (key, value) in s_json.items()]

yesterday_data = s_data_list[0]
yesterday_close_price = float(yesterday_data["4. close"])

day_before_data = s_data_list[1]
day_before_close_price = float(day_before_data["4. close"])

difference = (yesterday_close_price - day_before_close_price)
up_down = None
if difference > 0:
    up_down = "☝️"
else:
    up_down = "👇"

percentage = round((difference / yesterday_close_price) * 100)

print(percentage)

if abs(percentage) > 5:
    # Creating a connection with the New API
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    newsapi = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    newsapi.raise_for_status()
    newsapi_text = newsapi.text
    newsapi_json = json.loads(newsapi_text)
    articles = newsapi_json["articles"]
    three_articles = articles[:3]
    formated_articles_list = [f"\n{STOCK}: {up_down}{percentage}%\nHeadline: {article['title']}.\nNews: {article['description']}" for article in three_articles]

    # Creating a connecion with Twilio's API

    client = Client(twilio_sid_code, twilio_auth_code)

    for article in formated_articles_list:
        message = client.messages.create(
            body=article,  # --> Message that you want to send
            from_="",  # --> Twilio's Phone number
            to="")  # --> Personal Phone number
