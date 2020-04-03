import numpy as np
import argparse
import imutils
import cv2

def cember_ciz(frame,j,k,l,m,n,o):
    x = 0.0
    y = 0.0
    dusuk = {'kirmizi': (j, k, l) }
    yuksek = {'kirmizi': (m, n, o)}

    renkler = {'kirmizi': (255, 0, 0)}

    #frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    for key, value in yuksek.items():

        kernel = np.ones((9, 9), np.uint8)
        mask = cv2.inRange(hsv, dusuk[key], yuksek[key])
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(cnts) > 0:

            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


            if radius > 0.5:

                cv2.circle(frame, (int(x), int(y)), 5, (255,0,0), 2)
                cv2.putText(frame, " mavi light", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            renkler[key], 2)
    
    return frame,x,y
a=0
b=0
"""while True:
    ret,frame= kamera.read()
    frame,x,y = cember_ciz(frame)
    print(a,b)
    if x ==0 and y ==0:
        x = a
        y = b
    a = x
    b = y
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()
"""