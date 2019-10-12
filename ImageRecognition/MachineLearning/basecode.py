import cv2
import time

cap = cv2.VideoCapture(1)
i = 0

while(True and i < 75):
    # Capture frame-by-frame
    ret, frame = cap.read()
    i += 1
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    frame = cv2.resize(frame, (128, 128))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print('saving ', i)
    cv2.imwrite("train/wrong/" + str(i) + ".png", frame)
    time.sleep(0.5)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
