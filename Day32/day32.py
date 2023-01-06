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

"""

# Final Project
# Automated birthday wisher

import smtplib
import datetime

personal_email = ""  # --> Place in you're email
personal_email_password = ""  # --> Place in you're password
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=personal_email, password=personal_email_password)
    connection.sendmail(from_addr=personal_email,
                        to_addrs="", # --> Place in the e-mail that you want to send to the message
                        msg="Subject:Test\n\nThis is a test e-mail 2")
