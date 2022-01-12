#Face Detection Using Python
import cv2

cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

while True:
    #Capturing Frame
    ret, frame = cap.read()
    # More Operations
    gray = cv2.cvtColor(frame, 0)
    detections = cascade_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    if(len(detections) > 0):
        (x,y,w,h) = detections[0]
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # for (x,y,w,h) in detections:
    # 	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Displaying the Frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Realesing the Capture
cap.release()
cv2.destroyAllWindows()