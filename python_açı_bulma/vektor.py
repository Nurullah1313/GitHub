import cv2
import numpy as np
import math

#print(math.cos(math.radians(180)),math.degrees (math.acos (-1)))


o  = 0
x1 = 150
y1 = 50
z1 = 0
x2 = 50
y2 = 150
z2 = 0
a1 = abs(o-x1)
b1 = abs(o-y1)
c1 = abs(o-z1)
a2 = abs(o-x2)
b2 = abs(o-y2)
c2 = abs(o-z2)
mask = np.zeros([600,600])
cv2.line(mask,(o,o),(x1,y1),(255,255,255),2)
cv2.line(mask,(o,o),(x2,y2),(255,255,255),2)
d1 = math.sqrt((a1*a1)+(b1*b1)+(z1*z1))
d2 = math.sqrt((a2*a2)+(b2*b2)+(z2*z2))

dot = (x1*x2) + (y1*y2)
det = (x1*y2) - (x2*y1)
angle = math.atan2(det,dot)


skaler = ((a1*a2)+(b1*b2))
teta = math.degrees(math.acos(skaler/(d1*d2)))
print("cos(?) =",skaler/(d1*d2))
print("? = ",teta)
print("angle = ",angle)
cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()