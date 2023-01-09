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
import pandas
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row)  in data.iterrows()}


personal_email = ""  # --> Place in you're email
personal_email_password = ""  # --> Place in you're password

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, "r") as data:
        contents = data.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=personal_email, password=personal_email_password)
        connection.sendmail(from_addr=personal_email,
                            to_addrs=birthday_person["email"], # --> Place in the e-mail that you want to send to the message
                            msg=f"Subject:Happy B day mate !\n\n{contents}")
