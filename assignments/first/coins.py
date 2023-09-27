import cv2
import numpy as np

image = cv2.imread('./coins.png')  

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur the image 
blurred = cv2.GaussianBlur(gray_image, (15, 15), 0)
threshold_value = 155

# Apply binary thresholding
ret, binary_image = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY)

#invert the image
inverted_image = cv2.bitwise_not(binary_image)

# Find connected components in the inverted image
connectivity = 0 #
output = cv2.connectedComponentsWithStats(inverted_image, connectivity, cv2.CV_32S)

# Extract the connected components and their statistics
num_labels = output[0]
labels = output[1]
# Count the number of connected dark regions (islands)
num_of_coins = num_labels - 1  # Subtract 1 to exclude the background label

print(f"Number of coins: {num_of_coins}")