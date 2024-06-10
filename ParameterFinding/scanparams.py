import re
import os
def parameters_text(filecontent):
    pattern = r'"*([a-zA-Z_\. ]+)"*:"*([a-zA-Z_\. ]+)"*'
    current_line = ""
    key_value_pairs = []
    with open('params.txt', 'w') as file:
        file.write(filecontent)

    with open("params.txt", 'r') as file:
         content = ''.join(line.strip() for line in file)

# Write the modified content back to the file
    with open('input_file.txt', 'w') as file:
         file.write(content)
         with open('input_file.txt', 'r') as file:
              for line in file:
                   current_line += line.strip()
    matches = re.findall(pattern, current_line)
    for match in matches:
        key_value_pairs.append(match)
    unique_pairs = list(set(key_value_pairs))
# Write key-value pairs to a new text file
    with open('params_found.txt', 'w') as output_file:
        for key, value in unique_pairs:
            output_file.write(f"{key}: {value}\n")

# Specify the file path you want to remove
    file_path = 'input_file.txt'

# Check if the file exists before attempting to remove it
    if os.path.exists(file_path):
        os.remove(file_path)
        os.remove("params.txt")
        print(f"Cache files has been removed.")
    else:
        print(f"Cache files does not exist are not found.")
     
     
