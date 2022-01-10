#Screen Recorder Using Python
# Importing Required Modules
import pyautogui
import cv2
import numpy as np
  
# Defining Resoultion Of the Screen Recorder
resolution = (1920, 1080)
  
# Specifying Codec
codec = cv2.VideoWriter_fourcc(*"XVID")
  
# Defining the OutPut File Name
filename = "Screen-Recording.avi"
  
# Defining the FPS of the Screen Recording
fps = 60.0
  
  
# Video Wrier Windows
out = cv2.VideoWriter(filename, codec, fps, resolution)
  
# Creating an Empty Windows
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
  
# Defining Live Screen Resoulution
cv2.resizeWindow("Live", 480, 270)
  
while True:
    # Taking ScreenShot Using pyautogui module
    img = pyautogui.screenshot()
  
   # Converting the ScreenShot to Numpy Array
    frame = np.array(img)
  
    # RGB 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
    # Defining OutPut File
    out.write(frame)
      
    #Displaying the Screen Recording
    cv2.imshow('Live', frame)
      
    #Stop Screen Recording When 'q' Is Pressed
    if cv2.waitKey(1) == ord('q'):
        break
  
# Releaseing Video Writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()