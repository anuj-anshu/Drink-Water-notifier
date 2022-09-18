import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please! Drink Water.",
            message = "Drinking water is like washing out your insides. The water will cleanse the system, fill you up and decrease your caloric load",
            app_icon = "C:/Users/asdf/Desktop/Doc/icon.ico",
            timeout = 5
        )
        time.sleep(3600)