#Drink Water Notification Using Python
#importing Required Modules
import time
from plyer import notification
if __name__=="__main__":
  while True:
        notification.notify(title= "Drink Water Now!",
        message = "You Should Drink 7 Glass Water In a Day To Prevent Your Body From Dehydration",app_icon="ICON LOCATION",timeout = 12)
    
        time.sleep(30)
    
        
