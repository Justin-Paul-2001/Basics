# NOTE : Download a Sudoku Image from the Internet and store it in your system.
# NOTE : Convolution works Always on Gray Scale Image , so Colored image should be converted to Gray image.

import cv2

img = cv2.imread(r'C:\Users\ACER\Desktop\programming languages\Computer Vision\Oxysters-CV\Notes\sudoku.png',0)

sobel_x = cv2.Sobel(img , cv2.CV_8U , dx = 1 , dy = 0 , ksize = -1) # Vertical Lines are Detected -> dx = 1
sobel_y = cv2.Sobel(img , cv2.CV_8U , dx = 0 , dy = 1 , ksize = -1) # Horizontal Lines are Detected -> dy = 1
sobel_final = cv2.bitwise_or(sobel_x , sobel_y) # Convolution Of sobel_x , sobel_y

# 8U is actually saying 'uint8'
# dx = 1 is scrapping through y-axis and white lines are seen in it's place
# dy = 1 is scrapping through x-axis and white lines are seen in it's place

# Creation of Canny Edge Detected Image ->
canny = cv2.Canny(img , 100 , 255)

cv2.imshow("Sample Image",img)
cv2.imshow("Sobel_X Image",sobel_x)
cv2.imshow("Sobel_Y Image",sobel_y)
cv2.imshow("Final Sobel Image",sobel_final)

cv2.imshow("Canny Edge-Detect Image",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

