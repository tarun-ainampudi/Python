import cv2
import numpy as np

def split_image_by_characters(image_path, output_prefix="char"):
    """Splits an image into 6 parts, ensuring each part contains one character."""
    
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding (converts to black & white)
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Use morphological operations to close gaps
    kernel = np.ones((3,3), np.uint8)  # Adjust kernel size as needed
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours of characters
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours from left to right
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    # Ensure exactly 6 characters are detected
    if len(contours) != 6:
        print(f"Warning: Detected {len(contours)} characters instead of 6. Adjust thresholding or kernel.")
    
    char_images = []  # Store cropped character images

    for i, ctr in enumerate(contours):
        # Get bounding box of each character
        x, y, w, h = cv2.boundingRect(ctr)

        # Ignore small noise (adjust min width & height if needed)
        if w > 10 and h > 20:
            char_crop = img[y:y+h, x:x+w]  # Crop character
            char_images.append(char_crop)
            filename = f"{output_prefix}_{i+1}.png"
            cv2.imwrite(filename, char_crop)  # Save each character
            print(f"Saved: {filename}")  # Debugging statement

    return char_images  # Return list of character images

# Example usage
split_image_by_characters("output4.png")
