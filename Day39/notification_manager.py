from twilio.rest import Client

TWILIO_SID = ''    # Add in your Twilio's SID
TWILIO_AUTH_TOKEN = ''  # Add in your Twilio's Auth token
TWILIO_VIRTUAL_NUMBER = ""    # Add in your Twilio's virtual number
TWILIO_VERIFIED_NUMBER = ""    # Add in your phone number to send to


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