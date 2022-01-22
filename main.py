# Import statements
import cv2 as cv
import sys

# Reading an image into python using OpenCV

img = cv.imread(cv.samples.findFile("Images/pikachu.jfif"))  # Data is stored as cv::Mat

# Check to see if the image was loaded correctly
if img is None:
    sys.exit("Could not find the image :(")

# Display the image
cv.imshow("Photo", img)
k = cv.waitKey(0)  # "0" means wait forever

# Image is written to a file and the window is closed.
if k == ord("s"):
    cv.imwrite("Images/pikachu.png", img)  # Basically converted the image file into png
