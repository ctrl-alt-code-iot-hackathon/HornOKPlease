import cv2
import time

img_width = 128
img_height = 128

cap = cv2.VideoCapture(1)

i = 0
while(i<50):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()