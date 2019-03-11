import urllib
import cv2
import numpy as np
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://192.168.43.179:8080/shot.jpg'

while True:
    imgResp = urllib.urlopen(url)
    print('hit')
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('temp',cv2.resize(img,(600,400)))
    q = cv2.waitKey(1)
    if q == ord("q"):
        break;
    time.sleep(0.25)

cv2.destroyAllWindows()