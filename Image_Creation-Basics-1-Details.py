# If u are Using Python IDLE , Please make use u have the {cv2 library} installed .
# For Installation -> Open Command Prompt {cmd} -> Type - pip install open-cv python

import numpy as np
import cv2

b = np.zeros(10 , dtype = int) # Vector
print(b)

c = np.zeros([10,10] , dtype = int) # Matrix
print(c)

d = np.zeros([300,300]) # Black Image Pixel Initialisation

cv2.imshow("Black Background", d) # To display a image
                                  # Parameters of .imshow() ->
                                  # windname = Name of window
                                  # model created with matrix and values. 

cv2.waitKey(0) # This means it will wait till infinity if 0 is given as parameter till
               # any key is pressed . Otherwise the parameter is regarding no. of milliseconds
               # that the window will exist -> (2000) -> window stays for 2 seconds.

cv2.destroyAllWindows() # This will destroy any opened windows

e = np.ones([300,300]) # White Image Pixel Initialisation

cv2.imshow("White Background", e) # To display a image
cv2.waitKey(0)
cv2.destroyAllWindows()

##### NOTE : OpenCV follows BGR scale and {Not The RGB Scale}. #####

f = np.ones([300,300,3]) # RGB Image Pixel Initialisation
                         # We need a 3D plane for RGB-> Width , Height , (Depth = 3)
f[0:300,0:300] = [0,0,255]                         

##### NOTE : OpenCV follows BGR scale and {Not The RGB Scale} #####
# Hence [0,0,255] is for RED.

cv2.imshow("Red Background", f) # To display a image
cv2.waitKey(0)
cv2.destroyAllWindows()

g = np.ones([300,300,3]) # RGB Image Pixel Initialisation
                         # We need a 3D plane for RGB-> Width , Height , (Depth = 3)
g[0:300,0:300] = [0,255,255]

cv2.imshow("Random Background -> Yellow", g) # To display a image

cv2.waitKey(0)
cv2.destroyAllWindows()

h = np.ones([300,300,3])
h[0:300,0:300] = [255,0,255]

cv2.imshow("Random Background -> Pink", h) # To display a image
cv2.waitKey(0)
cv2.destroyAllWindows()

# NOTE : When we give the values of all R,G,B that is 0 or 255 , then there is a error.
#        We Have To manage the datatype ,so we use int8 which is 2^0 to 2^8.
#        But the issue is the value ranges from -127 to 128 ... so we are using
#        uint8 ->{unsigned int} which gives value from 0 to 255,

i = np.ones([300,300,3] , dtype = "uint8" )
i[0:300,0:300] = [50,100,150] # Use Of MS PAINT to Find RGB value of any color , but put
                              # it in reverse order for BGR scale.

cv2.imshow("Brown Background", i) # To display a image
cv2.waitKey(0)
cv2.destroyAllWindows()

# NOTE : If we want divide the background into various colours use the following method
#        to divide it different length and breadth -> 0:100 , 100:200 , 200:300.

j = np.ones([300,300,3] , dtype = "uint8" )

# uint16 can be also be used but the values range from 0 to 65536.

j[0:100,0:100] = [50,100,150]
j[0:100,100:200] = [50,200,150]
j[0:100,200:300] = [50,175,250]
j[100:200,0:100] = [70,100,250]
j[100:200,100:200] = [80,140,180]
j[100:200,200:300] = [90,200,100]
j[200:300,0:100] = [30,90,120]
j[200:300,100:200] = [80,160,240]
j[200:300,200:300] = [60,120,180]

cv2.imshow("Random Distributed Color Background", j) # To display a image
cv2.waitKey(0)
cv2.destroyAllWindows()
