"""
        LEARNING API'S (Application Programming Interface)

        Create a Kanye quote app

        from tkinter import *

        def get_quote():
            API = requests.get("https://api.kanye.rest")
            API.raise_for_status()
            data = API.text
            json_data = json.loads(data)
            random_quote = json_data["quote"]
            canvas.itemconfig(quote_text, text=random_quote)




        window = Tk()
        window.title("Kanye Says...")
        window.config(padx=50, pady=50)

        canvas = Canvas(width=300, height=414)
        background_img = PhotoImage(file="background.png")
        canvas.create_image(150, 207, image=background_img)
        quote_text = canvas.create_text(150, 207, text=f"", width=250, font=("Arial", 30, "bold"), fill="white")
        canvas.grid(row=0, column=0)

        kanye_img = PhotoImage(file="kanye.png")
        kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
        kanye_button.grid(row=1, column=0)



        window.mainloop()

"""
# Final project
# Create a project were we know were exactly the ISS is, and when it's above you, it will send you a message to look up
import json
import requests
import datetime as dt
import smtplib

PERSONAL_LATITUDE =   # --> You're Personal Latitude
PERSONAL_LONGITUDE =   # --> You're Personal Longitude


# Getting the ISS data
def is_iss_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.text
    json_data = json.loads(iss_data)

    iss_longitude = float(json_data['iss_position']['longitude'])
    iss_latitude = float(json_data['iss_position']['latitude'])

    if PERSONAL_LATITUDE - 5 <= iss_latitude <= PERSONAL_LATITUDE + 5 and PERSONAL_LONGITUDE - 5 <= iss_longitude <= PERSONAL_LONGITUDE + 5:
        return True


# Getting the sunrise data

def is_night():
    parameters_sunrise = {
        "lat": PERSONAL_LATITUDE,
        "lng": PERSONAL_LONGITUDE,
        "formatted": 0,
    }

    SUNRISE_API = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters_sunrise)
    SUNRISE_API.raise_for_status()
    sun_data = SUNRISE_API.text
    json_sun = json.loads(sun_data)
    sunrise = json_sun['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = json_sun['results']['sunset'].split('T')[1].split(':')[0]

    # Current time
    now = dt.datetime.now().hour

    # checking its dark time
    if now >= sunset or now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    personal_email = ""  # --> Place in you're email
    personal_email_password = ""  # --> Place in you're password

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=personal_email, password=personal_email_password)
        connection.sendmail(from_addr=personal_email,
                            to_addrs="", # --> Place in the e-mail that you want to send to the message
                            msg=f"Subject:Look overhead!\n\nLook up☝️👀!")
