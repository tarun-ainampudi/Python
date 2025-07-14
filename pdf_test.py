import pikepdf
from itertools import product

pdf_path = r"C:\Users\tarun\Downloads\8714693007930062025.pdf"

# Brute-force 11-digit numbers
for digits in product('0123456789', repeat=2):
    password = "181650101"+''.join(digits)
    print(f"Trying password: {password}")
    try:
        with pikepdf.open(pdf_path, password=password):
            print(f"[✓] Password found: {password}")
            break
    except pikepdf.PasswordError:
        pass
