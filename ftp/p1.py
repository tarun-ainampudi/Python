import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar

def list_files():
    """Fetch and display files from Android's storage."""
    directory = source_entry.get().strip()
    if not directory:
        messagebox.showerror("Error", "Please enter a directory path from your Android device.")
        return

    try:
        # Run adb shell command to list files
        result = subprocess.run(f'adb shell ls "{directory}"', shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            messagebox.showerror("Error", "Failed to fetch file list. Ensure ADB is connected.")
            return
        
        files = result.stdout.strip().split("\n")
        file_listbox.delete(0, tk.END)  # Clear previous list

        for file in files:
            file_listbox.insert(tk.END, file)
    
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching file list: {e}")

def pull_file():
    """Pull the selected file from Android to the laptop."""
    directory = source_entry.get().strip()
    selected_file = file_listbox.get(tk.ACTIVE)

    if not selected_file:
        messagebox.showerror("Error", "Please select a file to pull.")
        return
    
    destination = filedialog.askdirectory(title="Select Destination Folder")
    if not destination:
        return  # User canceled

    source_path = f"{directory}/{selected_file}"

    def run_adb():
        cmd = f'adb pull "{source_path}" "{destination}"'
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if process.returncode == 0:
            messagebox.showinfo("Success", f"File transferred successfully to {destination}!")
        else:
            messagebox.showerror("Error", f"Failed to transfer file:\n{process.stderr}")

    threading.Thread(target=run_adb, daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("ADB File Puller")
root.geometry("500x400")

# Directory input field
tk.Label(root, text="Enter Android Directory Path:").pack(pady=5)
source_entry = tk.Entry(root, width=50)
source_entry.pack(pady=5)
source_entry.insert(0, "/sdcard/Download")  # Default directory

# Fetch files button
tk.Button(root, text="List Files", command=list_files).pack(pady=5)

# Listbox to display files
frame = tk.Frame(root)
frame.pack(pady=5, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

file_listbox = Listbox(frame, width=60, height=10, yscrollcommand=scrollbar.set)
file_listbox.pack(pady=5, fill=tk.BOTH, expand=True)

scrollbar.config(command=file_listbox.yview)

# Pull file button
tk.Button(root, text="Select Destination & Pull File", command=pull_file).pack(pady=10)

root.mainloop()
