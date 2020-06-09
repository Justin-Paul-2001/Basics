import cv2

capture = cv2.VideoCapture(0)

while True:
    sample , frame = capture.read()
    
    # 'sample' is a variable that is written bcoz.
    # capture.read() needs 2 variables assignment.
    # Not Of much Use -> 'sample' variable.

    frame = cv2.flip(frame , 1) # For Flipping Images ->
                                # 1 -> Lateral inversion {left becomes right}.
                                
    cv2.imshow("Output Video" , frame)
    if cv2.waitKey(1) == 27 : # 'esc' key is used to break loop.
        break

if capture.isOpened():
    sample , frame_new = capture.read()

cv2.imshow("Captured Image" , frame_new)
cv2.waitKey(0)

###### IMPORTANT #######

#### MUST WRITE ###
    
capture.release() # To Switch Off WebCam

###################

cv2.destroyAllWindows()
