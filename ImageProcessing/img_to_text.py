from PIL import Image
import pytesseract
import pandas as pd

def get_text(input_path: str):
    img = Image.open(input_path).convert("L")
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    text = pytesseract.image_to_string(img,config=custom_config)
    return text

# Process multiple images
for i in range(1, 6):
    print(f"Processing output{i}.png")
    df = get_text(f"output{i}.png")  # Store DataFrame if needed
    print(df)
