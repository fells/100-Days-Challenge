from twilio.rest import Client

TWILIO_SID = 'AC839b8e9a2ef65ed70dd92bd024d8332c'
TWILIO_AUTH_TOKEN = '0a392c84ad5ac38724796e31791681d8'
TWILIO_VIRTUAL_NUMBER = "+19302057371"
TWILIO_VERIFIED_NUMBER = "+5521981289048"


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