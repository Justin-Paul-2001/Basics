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

############################################################################################

# New Program #

import cv2
import numpy as np

img = np.ones([800,800], dtype ='uint8') * 255 # Creating A Background
img[100:700,100:700] = 0 # Creating A Canvas

window_name = "Canvas Functionality"
cv2.namedWindow(window_name)
abc = False # DEFINING A FLAG 

def draw_eraser(event , x , y , flags , param):
      global abc # To use a Variable That Is Defined Outside the Function.
      if event == cv2.EVENT_LBUTTONDOWN:
        abc = True
        cv2.circle(img,(x,y),2,(255,255,255),-1)
      elif event == cv2.EVENT_MOUSEMOVE:
        if (abc == True):
            cv2.circle(img,(x,y),2,(255,255,255),-1)
      else:
            abc = False

cv2.setMouseCallback(window_name,draw_eraser) # CallBack Method
while True:
    cv2.imshow( window_name , img)
    key = cv2.waitKey(1) 
    if key == ord('q'): # TO REMOVE / SWITCH OFF THE CANVAS
        break
    elif key == ord('c'): # CLEARING THE CANVAS BACK TO ORIGINAL FORM
        img[100:700,100:700] = 0
    elif key == ord('w'): # SAVING THE CANVAS IMAGE 
        output_img = img[100:700,100:700]
        cv2.imwrite("Output Image.jpg" , output_img )
    
cv2.destroyAllWindows()
