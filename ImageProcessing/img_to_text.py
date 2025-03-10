from PIL import Image
import pytesseract
import pandas as pd

def get_text(path):
    img = Image.open(path).convert("RGBA")

    # Custom OCR config with character whitelist
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Get OCR data as a DataFrame
    df = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME, config=custom_config)

    # Remove empty and low-confidence results
    df = df[df['conf'] > 50]  # Keep only high-confidence detections
    df = df.dropna(subset=['text'])  # Remove empty text rows

    # Extract final text
    text = " ".join(df['text'].astype(str))  # Join words into a string

    print(f"pytesseract: {text}")
    return df  # Return DataFrame for further analysis if needed

# Process multiple images
for i in range(1, 6):
    print(f"Processing output{i}.png")
    df = get_text(f"output{i}.png")  # Store DataFrame if needed
    print(df)
