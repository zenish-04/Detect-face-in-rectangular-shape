import sys
import cv2

def detect_faces(frame):
    cascade_path=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
    detector=cv2.CascadeClassifier(cascade_path)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    for(x,y,w,h) in detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5):
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    return frame

capture=cv2.VideoCapture(0)
if capture.isOpened()==False:
    print("Error opening webcam")
    sys.exit(1)

while True:
    ret,frame=capture.read()
    if ret==False:
        break
    cv2.imshow("Face detection", detect_faces(frame))
    if cv2.waitKey(1) & 0xFF in (27,):
        break
capture.release()
cv2.destroyAllWindows()
