# Battery Notifier Using Python
# importing required Modules
#plyer or pip install plyer & psutil or pip install psutil
from plyer import notification
import psutil 

# psutil.sensors_battery() will return the information related to battery
battery = psutil.sensors_battery()

# battery percent will return the current battery prcentage
battery_percent = battery.percent
charging = battery.power_plugged

# Notification(title, description, duration)--to send
# notification to desktop
#help(Notification)
if charging:
    if battery_percent == 100:
        charging_message = "Unplug your Charger"
    else:
        charging_message = "Charging"
else:
    charging_message = "Not Charging"
message = str(battery_percent)+ "% Charged\n" + charging_message

notification.notify("Battery Information", message, timeout = 10)