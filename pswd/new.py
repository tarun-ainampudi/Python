import torch
import itertools
import string
import pikepdf
from concurrent.futures import ThreadPoolExecutor

# PDF path
pdf_file = r"C:\Users\tarun\Downloads\6137.pdf"

def verify_password(pwd):
    try:
        with pikepdf.open(pdf_file, password=pwd) as pdf:
            pdf.save("decrypted_bob.pdf")
            print(f"[+] Password found: {pwd}")
            return True
    except:
        print(f"[-] Password {pwd} is incorrect.")
        return False

def generate_passwords_on_gpu(batch_size=1000):
    # Move characters to GPU
    letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    total = 26**4 * 10**4
    print(f"Total combinations: {total}")

    def index_to_password(idx):
        prefix = []
        for _ in range(4):
            prefix.append(letters[idx % 26])
            idx //= 26
        prefix = prefix[::-1]
        suffix = f"{idx:04d}"
        return ''.join(prefix) + suffix

    for start in range(0, total, batch_size):
        indices = torch.arange(start, min(start + batch_size, total), device=device)
        passwords = [index_to_password(int(i.item())) for i in indices]
        yield passwords

found_flag = False

def check_batch(passwords):
    global found_flag
    for pwd in passwords:
        if found_flag:
            return
        if verify_password(pwd):
            found_flag = True
            break

with ThreadPoolExecutor(max_workers=8) as executor:
    for batch in generate_passwords_on_gpu(batch_size=5000):
        if found_flag:
            break
        executor.submit(check_batch, batch)
