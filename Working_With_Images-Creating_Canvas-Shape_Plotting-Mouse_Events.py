import cv2
import numpy as np

img = np.ones([400,400,3], dtype ='uint8') * 255 # Scalar Multiplication -> { * 255}
                                                 # This will give a White Background.
window_name = "Drawing"
cv2.namedWindow(window_name)

def draw_shape(event , x , y , flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
       cv2.circle(img,(x,y),50,(60,120,180),-5)
       print(f"The Center of Circle is {x},{y} with radius 50")
    if event == cv2.EVENT_RBUTTONDOWN:
       cv2.rectangle(img,(x,y),(x+100,y+100),(40,120,240),5)

########## IMPORTANT ##########

##### CALLING THE FUNCTION ####
       
cv2.setMouseCallback(window_name,draw_shape) # CallBack Method

###############################

while True:
    cv2.imshow( window_name , img)
    if cv2.waitKey(1) == 27 : # 27 is the ascii value of 'escape key' -> Esc Key
        break
    
cv2.destroyAllWindows()
