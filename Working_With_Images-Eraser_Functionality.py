import cv2
import numpy as np

img = np.zeros([600,600,3], dtype ='uint8')

window_name = "Eraser Tool"
cv2.namedWindow(window_name)
abc = False # DEFINING A FLAG 

def draw_eraser(event , x , y , flags , param):
      global abc
      if event == cv2.EVENT_LBUTTONDOWN:
        abc = True
        cv2.circle(img,(x,y),2,(255,255,255),-1)
      elif event == cv2.EVENT_MOUSEMOVE:
        if (abc == True):
            cv2.circle(img,(x,y),2,(255,255,255),-1)
      else:
            abc = False

########## IMPORTANT ##########

cv2.setMouseCallback(window_name,draw_eraser) # CallBack Method

###############################

while True:
    cv2.imshow( window_name , img)
    if cv2.waitKey(1) == 27 : # 27 is the ascii value of 'escape key' -> Esc Key
        break
    
cv2.destroyAllWindows()

