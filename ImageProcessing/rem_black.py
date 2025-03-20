import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("output1.png", cv2.IMREAD_COLOR)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding to create a mask (black areas become 0, others become 255)
_, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# Convert mask to 3 channels
mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

# Apply the mask to remove the black background
result = cv2.bitwise_and(img, mask_3ch)

# Show the result
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Black Background Removed")
plt.axis("off")

plt.show()
