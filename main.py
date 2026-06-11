import time
from plyer import notification

while True:
    print("Plese Drink Some Water........")
    notification.notify(title="Water Reminder", message="You need to drink some water to keep your body hydrated......")

    time.sleep(60*60)