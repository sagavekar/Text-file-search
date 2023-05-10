import tkinter as tk
from tkinter import filedialog
import re
import os

flag_found = 0

def select_files():
    initial_dir = os.path.expanduser("~")  # Set initial directory to user's home directory
    files = filedialog.askopenfilenames(initialdir=initial_dir, filetypes=[("Text Files", "*.txt")])
    file_list.delete(0, tk.END)  # Clear the existing list
    for file_path in files:
        file_name = os.path.basename(file_path)
        file_list.insert(tk.END, file_name)

def search_files():
    keyword = keyword_entry.get()
    file_matches.delete(0, tk.END)  # Clear the existing list

    for i in range(file_list.size()):
        file_name = file_list.get(i)
        file_path = os.path.join(current_dir, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            matches = re.findall(keyword, content)
            if matches:
                flag_found = 1
                file_matches.insert(tk.END, file_name)

window = tk.Tk()
window.title("Text File Search")

# Styling
window.geometry("500x400")
window.configure(background="#F0F0F0")

# File Selection
file_frame = tk.Frame(window, bg="#F0F0F0")
file_frame.pack(pady=5)

file_list = tk.Listbox(file_frame, selectmode=tk.MULTIPLE, font=("Arial", 11), width=60, height=6)
file_list.pack(fill=tk.BOTH, expand=True)

file_button = tk.Button(file_frame, text="Select Files", command=select_files, font=("Arial", 12))
file_button.pack (side="bottom",pady=3)

# Keyword Search
keyword_frame = tk.Frame(window, bg="#F0F0F0")
keyword_frame.pack(pady=5)

keyword_label = tk.Label(keyword_frame, text="Keyword:", bg="#F0F0F0", font=("Arial", 12))
keyword_label.pack(side=tk.LEFT)

keyword_entry = tk.Entry(keyword_frame, font=("Arial", 11), width=30)
keyword_entry.pack(side=tk.LEFT)

search_button = tk.Button(window, text="Search", command=search_files, font=("Arial", 12))
search_button.pack(pady=5)

# Result Display
result_label = tk.Label(window, text="Matching Files:", bg="#F0F0F0", font=("Arial", 12))
result_label.pack()

file_matches = tk.Listbox(window, font=("Arial", 11), width=50, height=8)
file_matches.pack(fill=tk.BOTH, expand=True)

# Get the current directory
current_dir = os.getcwd()

window.mainloop()
