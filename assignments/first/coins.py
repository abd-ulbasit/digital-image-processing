import cv2
import numpy as np

image = cv2.imread('./coins.png')  # Replace 'your_image.jpg' with the path to your image file
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",gray_image)
blurred = cv2.GaussianBlur(gray_image, (15, 15), 0)
threshold_value = 155

# Apply binary thresholding
ret, binary_image = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY)

new_width = 200  # Replace with your desired width
new_height = 200  # Replace with your desired height

# Resize the image to the new dimensions
resized_image = cv2.resize(binary_image, (new_width, new_height))
# Display the binary image
# cv2.imshow("resized_image", resized_image)
upsized=cv2.resize(resized_image,(600,600))
pix=np.array(resized_image)
for p in pix:
    print(p)
# cv2.imshow("Upsized",upsized)
inverted_image = cv2.bitwise_not(upsized)

# Find connected components in the inverted image
connectivity = 0  # Use 4-connectivity for counting connected regions
output = cv2.connectedComponentsWithStats(inverted_image, connectivity, cv2.CV_32S)

# Extract the connected components and their statistics
num_labels = output[0]
labels = output[1]
print(output)
# Count the number of connected dark regions (islands)
num_islands = num_labels - 1  # Subtract 1 to exclude the background label

print(f"Number of islands (connected dark regions): {num_islands}")
cv2.waitKey(0)
cv2.destroyAllWindows()
# blurred = cv2.GaussianBlur(gray, (15, 15), 0)
# cv2.imshow("blurred",blurred)
# circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=50)

# cv2.imshow("Circles",circles)
# if circles is not None:
#     # Convert the (x, y) coordinates and radius of the circles to integers
#     circles = np.round(circles[0, :]).astype("int")
    
#     # Loop over the detected circles and draw them on the original image
#     for (x, y, r) in circles:
#         cv2.circle(image, (x, y), r, (0, 255, 0), 4)  # Draw the circle in green
#         cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)  # Draw the center of the circle in orange

#     # Print the number of detected circles (coins)
#     num_coins = len(circles)
#     print(f"Number of coins detected: {num_coins}")
    
#     # Display the image with detected circles
#     cv2.imshow("Detected Coins", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("No coins detected.")


