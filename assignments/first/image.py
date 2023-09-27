import cv2

# Load the RGB image
image = cv2.imread('./wolf.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image to create a binary image
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Save the grayscale image
cv2.imwrite('gray_image.jpg', gray_image)

# Save the binary image
cv2.imwrite('binary_image.jpg', binary_image)

# Display the grayscale and binary images (optional)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Binary Image', binary_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
