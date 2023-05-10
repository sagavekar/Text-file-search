import tkinter as tk
from tkinter import filedialog
import re
import os


def select_files():
    initial_dir = os.path.expanduser("~")  # Set initial directory to user's home directory
    files = filedialog.askopenfilenames(initialdir=initial_dir, filetypes=[("Text Files", "*.txt")])
    file_list.delete(0, tk.END)  # Clear the existing list
    for file_path in files:
        file_name = os.path.basename(file_path)
        file_list.insert(tk.END, file_name)

    if files:
        global current_dir
        current_dir = os.path.dirname(files[0])

def search_files():
    keyword = keyword_entry.get()
    file_matches.delete(0, tk.END)  # Clear the existing list

    match_found = False  # Variable to track if any match is found

    for i in range(file_list.size()):
        file_name = file_list.get(i)
        file_path = os.path.join(current_dir, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            matches = re.findall(keyword, content)
            if matches:
                file_matches.insert(tk.END, file_name)
                match_found = True

    if not match_found:
        file_matches.insert(tk.END, "No match found, Plese note that Keyword in case sensative")

def clear_all():
    file_list.delete(0, tk.END)
    keyword_entry.delete(0, tk.END)
    file_matches.delete(0, tk.END)

window = tk.Tk()
window.title("Text File Search | Omka Sagavekar | TSO-SET ")

# Styling
window.geometry("500x300")
window.configure(background="#F0F0F0")

# File Selection
file_frame = tk.Frame(window, bg="#F0F0F0")
file_frame.pack(pady=5)

file_list = tk.Listbox(file_frame, selectmode=tk.MULTIPLE, font=("Arial", 11), width=600, height=6)
file_list.pack(fill=tk.BOTH, expand=True)


# Button Frame
button_frame = tk.Frame(file_frame, bg="#F0F0F0")
button_frame.pack(pady=5)

select_button = tk.Button(button_frame, text="Select Files", command=select_files, font=("Arial", 12))
select_button.pack(side=tk.LEFT, padx=20, pady=5)

search_button = tk.Button(button_frame, text="Search", command=search_files, font=("Arial", 12))
search_button.pack(side=tk.LEFT, padx=20, pady=5)

clear_button = tk.Button(button_frame, text="Reset", command=clear_all, font=("Arial", 12))
clear_button.pack(side=tk.LEFT, padx=20, pady=5)


# Keyword Search
keyword_frame = tk.Frame(window, bg="#F0F0F0")
keyword_frame.pack(pady=5)

keyword_label = tk.Label(keyword_frame, text="Keyword:", bg="#F0F0F0", font=("Arial", 12))
keyword_label.pack(side=tk.LEFT)

keyword_entry = tk.Entry(keyword_frame, font=("Arial", 11), width=30)
keyword_entry.pack(side=tk.LEFT)



# Result Display
result_label = tk.Label(window, text="Matching Files:", bg="#F0F0F0", font=("Arial", 12))
result_label.pack()

file_matches = tk.Listbox(window, font=("Arial", 11), width=50, height=8)
file_matches.pack(fill=tk.BOTH, expand=True)



window.mainloop()
