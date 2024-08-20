import pytesseract
from PIL import Image


# Load the image
image_path = r"C:\Users\tarun\Desktop\Python\Image to text\captcha.jpg"
image = Image.open(image_path)

# Use Tesseract to extract text
captcha_text = pytesseract.image_to_string(image)

print("CAPTCHA text:", captcha_text)
