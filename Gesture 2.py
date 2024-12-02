import cv2
cap = cv2.VideoCapture("output.avi")
cap.set(1, 320)
ret, frame = cap.read()
cv2.imwrite("frame2.jpg", frame)
