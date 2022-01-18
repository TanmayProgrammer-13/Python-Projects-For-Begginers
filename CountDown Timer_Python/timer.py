#Importing Modules
import time


#Creting a Funtion
def CountDown(t):
    while t:
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1

        print("Timer Finished!")


        time = input("Enter the Duration In Seconds: ")

        CountDown(int(t))