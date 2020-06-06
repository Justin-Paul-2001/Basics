import numpy as np
import cv2

# Creating A Chessboard Type Image / CheckerBoard ->

checkerboard = np.zeros([400,400],dtype = 'uint8')
print(checkerboard.ndim)
# 2 variable - i -rows, j - columns

for i in range(0,401,100):
    for j in range(0,401,100):
        checkerboard[i:i+50,j:j+50] = 255

for i in range(50,401,100):
    for j in range(50,401,100):
        checkerboard[i:i+50,j:j+50] = 255
        
cv2.imshow('Checkerboard Image',checkerboard)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Reading A Image From User System
img = cv2.imread(r'C:\Users\ACER\Desktop\programming languages\Computer Vision\Oxysters-CV\Notes\Sample-Image.png')
print(img.shape)
print(img.size)

# Creating A Gray Scale Image
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

# Converting Image Scale To RGB Scale
rgb_img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

# Writing Text Inside the Image
cv2.putText(rgb_img , "Justin's Image" , (60,50) , cv2.FONT_HERSHEY_COMPLEX , 2 , (0,0,255) , 1)
# Parameters of .putText() ->
# 1st parameter -> Source of Image
# 2nd parameter -> Text to Be Written
# 3rd parameter -> Initialise the Starting point in terms of pixel point.
# 4th Parameter -> Name of the Font
# 5th Parameter -> Size of text
# 6th Parameter -> Color of text
# 7th Parameter -> Thickness of text.


cv2.imshow('Original Image' , img)
cv2.imshow('GrayScale Image' , gray_img)
cv2.imshow('RGBScale Image' , rgb_img)

# Creating and Saving a Duplicate Copy of the Image.
cv2.imwrite('Duplicate RGB Image.png', rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
