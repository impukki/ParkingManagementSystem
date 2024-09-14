import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

# Capture a frame from the camera
ret, frame = cap.read()

# Save the frame to a file
cv2.imwrite('img.jpg', frame)

# Release the camera
cap.release()
