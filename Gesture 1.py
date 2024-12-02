import cv2
cap = cv2.VideoCapture("output.avi")
cap.set(1, 300)
ret, frame = cap.read()
cv2.imwrite("frame.jpg", frame)
