from twilio.rest import Client
import smtplib

TWILIO_SID = ''    # Add in your Twilio's SID
TWILIO_AUTH_TOKEN = ''  # Add in your Twilio's Auth token
TWILIO_VIRTUAL_NUMBER = ""    # Add in your Twilio's virtual number
TWILIO_VERIFIED_NUMBER = ""    # Add in your phone number to send to

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com" # --> Place in you're email SMTP server
MY_EMAIL = "" # --> Place in you're email
MY_PASSWORD = "" # --> Place in you're password

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )