import cv2
import numpy as np

def nothing(x):
    pass

img = np.ones([400,400,3], dtype ='uint8') * 255 # Scalar Multiplication -> { * 255}
                                                 # This will create a white background.

cv2.line(img,(0,0),(400,400),(0,255,0),5)
# Parameters of .line() ->
# 1st Parameter -> Source / Background Image
# 2nd Parameter -> Starting Point of Line
# 3rd Parameter -> End Point of Line
# 1st Parameter -> Color of Line
# 1st Parameter -> Thickness of Line

cv2.circle(img,(100,100),50,(60,120,180),15)
# Parameters of .circle() ->
# 1st Parameter -> Source / Background Image
# 2nd Parameter -> Center Of Circle
# 3rd Parameter -> Radius Of Circle
# 1st Parameter -> Color Of Circle
# 1st Parameter -> Thickness Of Circle

cv2.rectangle(img,(175,175),(275,275),(40,120,240),15)
# Parameters of .rectangle() ->
# 1st Parameter -> Source / Background Image
# 2nd Parameter -> Top Diagonal Co-ordinate Of Rectangle
# 3rd Parameter -> Bottom Diagonal Co-ordinate Of Rectangle
# 1st Parameter -> Color Of Rectangle
# 1st Parameter -> Thickness Of Rectangle

########

# NOTE : IF THE THICKNESS IS GIVEN AS NEGATIVE , THEN IT WILL FILL THE WHOLE FIGURE.

cv2.rectangle(img,(200,0),(250,100),(40,120,240),-5)

########

i = 0
while True:
    cv2.circle(img,(i+100,i),20,(200,20,200),5)
    cv2.line(img,(0,i),(400,0),(0,200,200),1)
    cv2.circle(img,(i,i+100),20,(200,20,200),5)
    i += 20
    cv2.imshow("Shape Image" , img)
    if cv2.waitKey(1) == 27 : # 27 is the ascii value of 'escape key' -> Esc Key
        break
    
cv2.destroyAllWindows()
