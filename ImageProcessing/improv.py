import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def restore_text(image_path):
    """Preprocess and restore broken letters for better OCR"""
    
    # Load Image in Grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Adaptive Thresholding
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Use Morphological Operations to close gaps
    kernel = np.ones((3,3), np.uint8)  # Adjust kernel size for better results
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Dilate to reconnect broken parts
    dilated = cv2.dilate(morph, kernel, iterations=1)

    return dilated



for i in range(1,6):
    restored_img = restore_text(f"output{i}.png")
    restored_img = Image.open(restored_img).convert("L")
    cv2.imwrite(f"restored_output{i}.png", restored_img)
    restored_img = restore_text(f"captcha{i}.jpeg")
    restored_img = Image.open(restored_img).convert("L")
    cv2.imwrite(f"restored_captcha{i}.png", restored_img)

