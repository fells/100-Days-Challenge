import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt", "r") as data:
    quotes = data.read()
    quotes_into_list = quotes.split('\n')
    for q in quotes_into_list:
        random_quote = random.choice(quotes_into_list)

if day_of_week == 0:
    personal_email = ""  # --> Place in you're email
    personal_email_password = ""  # --> Place in you're password
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=personal_email, password=personal_email_password)
        connection.sendmail(from_addr=personal_email,
                            to_addrs="", # --> Place in the e-mail that you want to send to the message
                            msg=f"Subject:Motivational Thursday\n\n{random_quote}")