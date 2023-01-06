"""
            Learning how to use SMTPLIB

            personal_email = ""  --> Place in you're email
            personal_email_password = ""  --> Place in you're password
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=personal_email, password=personal_email_password)
                connection.sendmail(from_addr=personal_email,
                                    to_addrs="", --> Place in the e-mail that you want to send to the message
                                    msg="Subject:Test\n\nThis is a test e-mail 2")


            LEARNING DATETIME LIB


            now = dt.datetime.now()
            year = now.year
            month = now.month
            day = now.day
            day_of_week = now.weekday()
            print(day_of_week)

            DOB = dt.datetime(year=1997,month=4,day=23)
            DOB_YEAR = DOB.year
            DOB_MONTH = DOB.month
            DOB_DAY = DOB.day

            EXERCISE 1


            Create an automated motivational message sender for a specif day

            now = dt.datetime.now()
            day_of_week = now.weekday()

            with open("quotes.txt", "r") as data:
                quotes = data.read()
                quotes_into_list = quotes.split('\n')
                for q in quotes_into_list:
                    random_quote = random.choice(quotes_into_list)

            if day_of_week == 3:
                personal_email = ""  # --> Place in you're email
                personal_email_password = ""  # --> Place in you're password
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=personal_email, password=personal_email_password)
                    connection.sendmail(from_addr=personal_email,
                                        to_addrs="", # --> Place in the e-mail that you want to send to the message
                                        msg=f"Subject:Motivational Thursday\n\n{random_quote}")

"""
# Final Project
# Automated birthday wisher

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as data:
        quotes = data.read()
        quotes_into_list = quotes.split('\n')
        for q in quotes_into_list:
            random_quote = random.choice(quotes_into_list)

    personal_email = ""  # --> Place in you're email
    personal_email_password = ""  # --> Place in you're password
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=personal_email, password=personal_email_password)
        connection.sendmail(from_addr=personal_email,
                            to_addrs="", # --> Place in the e-mail that you want to send to the message
                            msg=f"Subject:Motivational Monday\n\n{random_quote}")
