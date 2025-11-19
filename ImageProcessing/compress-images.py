from math import ceil
import os
from PIL import Image
import subprocess


def compress_image(input_path: str):

    if not os.path.exists(input_path):
        print(f"The path {input_path} does not exist.")
        return

    output_path = ""

    for i in range(len(input_path.split("\\"))):
        if i == len(input_path.split("\\"))-1:
            continue
        else:
            output_path += input_path.split("\\")[i] + "\\"

    output_path += "Compressed-"+input_path.split("\\")[-1]
    print(input_path)
    print(output_path)

    os.makedirs(output_path, exist_ok=True)

    for file in os.listdir(input_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')):
            img_path = os.path.join(input_path, file)
            out_file = os.path.join(output_path, file)
            try:
                with Image.open(img_path) as img:
                    org_width, org_height = img.size
                    # if org_width > org_height:
                    #     new_width = 2160
                    #     new_height = ceil((new_width / org_width) * org_height)
                    # else:
                    #     new_height = 2160
                    #     new_width = ceil((new_height / org_height) * org_width)
                    new_height = 1754
                    new_width = 1250   
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
                continue
            subprocess.run(["cwebp", "-resize",str(new_width),str(new_height),str(img_path), "-o", str(out_file)], check=True)
            print(f"Resizing {file} from ({org_width}, {org_height}) to ({new_width}, {new_height})")
        else:
            print(f"Skipping non-image file: {file}")
            continue


compress_image(r"C:\Users\tarun\Downloads\Compressed-DL-DA01")
