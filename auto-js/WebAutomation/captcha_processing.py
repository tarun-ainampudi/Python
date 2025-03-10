from PIL import Image
import pytesseract
import urllib.request

def download_image_urllib(url: str, save_path: str) -> None:
    """
    Downloads an image from the specified URL using urllib and saves it to the given path.
    
    :param url: The URL of the image to download.
    :param save_path: The file path (including filename) where the image will be saved.
    """
    urllib.request.urlretrieve(url, save_path)


def remove_white_from_image(input_path: str, output_path: str, threshold: int = 140) -> None:
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
    img = img.convert("L")#converting to grey scale
    img.save(output_path)
    
# def img_to_text(input_path: str):
#     img = Image.open(input_path).convert("L")
#     custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     df = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME, config=custom_config)
#     df = df[df['conf'] > 50]  # Keep only high-confidence detections
#     df = df.dropna(subset=['text'])  # Remove empty text rows
#     text = " ".join(df['text'].astype(str))  # Join words into a string
#     return text

def img_to_text(input_path: str):
    img = Image.open(input_path).convert("L")
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    text = pytesseract.image_to_string(img,config=custom_config)
    return text