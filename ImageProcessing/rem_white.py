from PIL import Image
import pytesseract
import easyocr
import numpy as np


def remove_white_from_image(input_path: str, output_path: str, threshold: int = 60) -> None:
    """
    Removes white (or near-white) pixels from an image by setting their alpha value to 0.
    
    Parameters:
    - input_path: Path to the input image file.
    - output_path: Path where the processed image will be saved.
    - threshold: An integer (0-255) used to determine what counts as "white". 
                 Pixels with RGB values above this threshold will be made transparent.
    """
    # Load image and ensure it has an alpha channel
    img = Image.open(input_path).convert("RGBA")
    pixels = img.getdata()
    
    new_pixels = []
    for pixel in pixels:
        # Check if red, green, and blue values are high enough to be considered white
        if pixel[0] > threshold and pixel[1] > threshold and pixel[2] > threshold:
            # Change white pixel to transparent
            new_pixels.append((255, 255, 255, 0))
        else:
            new_pixels.append(pixel)

    img.putdata(new_pixels)
    #img = img.convert("L")#converting to grey scale
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    text = pytesseract.image_to_string(img,config=custom_config)
    print(f"pytesseract : {text}")    
    #reader = easyocr.Reader(['en']) 
    #result = reader.readtext(np.array(img), detail=0)
    #print(f"easyocr : {text}")
    img.save(output_path)

# Example usage:
# for i in range(1,6):
#     remove_white_from_image(f"captcha{i}.jpeg",f"output{i}.png")

# remove_white_from_image(r"C:\Users\tarun\Downloads\Signature.jpg","Signature_output.png",200)