import cv2
import numpy as np
img = cv2.imread("girilmez.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thrash = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approax = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approax], 0 ,[0,0,0], 1)
    x = approax.ravel() [0]
    y = approax.ravel() [1]
    if len(approax) == 3:
        cv2.putText(img, "ucgen", (x, y + 60), cv2.FONT_HERSHEY_COMPLEX, (0.5), (0, 0, 0))
    if len(approax) == 4:
        cv2.putText(img, "dortgen", (x, y + 60), cv2.FONT_HERSHEY_COMPLEX, (0.5), (0, 0, 0))
    if len(approax) == 5:
        cv2.putText(img,"besgen",(x,y+60),cv2.FONT_HERSHEY_COMPLEX,(0.5),(0,0,0))
    if len(approax) == 6:
        cv2.putText(img, "altıgen", (x, y + 60), cv2.FONT_HERSHEY_COMPLEX, (0.5), (0, 0, 0))
    if len(approax) > 8:
        cv2.putText(img,"daire",(x,y+60),cv2.FONT_HERSHEY_COMPLEX,(0.5),(0,0,0))

cv2.imshow("geometric",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
