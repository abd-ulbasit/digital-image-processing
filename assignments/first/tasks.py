import cv2

# Load the RGB image
image = cv2.imread('./wolf.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image to create a binary image !! fine-tuned the threshold 

_, binary_image = cv2.threshold(gray_image, 148, 255, cv2.THRESH_BINARY)
scaling_factor = 0.5  # Change this to own desired factor

# Resize the image while maintaining the aspect ratio
resized_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)

# Save the resized image
cv2.imwrite('output.jpg', resized_image)

# Display the resized image (optional)
cv2.imshow('Resized Image', resized_image)
# Save the grayscale image
cv2.imwrite('gray_image.jpg', gray_image)

# Save the binary image
cv2.imwrite('binary_image.jpg', binary_image)

# Display the grayscale and binary images (optional)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Binary Image', binary_image)

# Wait for a key press and then close the windows
key=cv2.waitKey(0)
while key!=ord(" "):
    key=cv2.waitKey(0)
cv2.destroyAllWindows()
