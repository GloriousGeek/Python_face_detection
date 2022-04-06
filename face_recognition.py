#importing opencv
import cv2

#using cv2.CascadeClassifier and accessing haarcascade_frontalface_default.xml to detect face
faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("sample_image.jpg")

#changing the image to gray scale for better face detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#specificying the search detection using detectMultiScale
multi_scale = faces.detectMultiScale(gray,
scaleFactor = 1.05,
minNeighbors = 5)

#drawing a rectangle to the image.
#for loop is used to access all the coordinates of the rectangle.
for x, y, w, h in multi_scale:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 5)

#showing the detected face followed by the waitKey method.
cv2.imshow("usman_tariq", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
