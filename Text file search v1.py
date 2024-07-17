import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import re
import os
import subprocess
from datetime import date


def select_files():
    
    initial_dir = os.path.expanduser("~")  # Set initial directory to user's home directory
    files = filedialog.askopenfilenames(initialdir=initial_dir, filetypes=[("All files", "*")])
    file_list.delete(0, tk.END)  # Clear the existing list
    
    file_count = len(files)
    file_count_label.config(text=f"{file_count}")
    
    
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
    num_files = file_list.size()

    for i in range(num_files):
        file_name = file_list.get(i)
        file_path = os.path.join(current_dir, file_name)
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                content = file.read()
                matches = re.findall(keyword, content)
                if matches:
                    file_matches.insert(tk.END, file_name)
                    match_found = True
        except (IOError, OSError) as e:
            file_matches.insert(tk.END, f"Error reading file: {file_name}")
            print(f"Error reading file: {file_name}")
            print(e)
        except:
            print(f"Some error at {file_path}")

    file_matches.bind("<Double-Button-1>", open_selected_file)

    
    if not match_found:
        file_matches.insert(tk.END, "No match found. Please note that the keyword is case-sensitive.")
        



def open_selected_file(event):
    selected_file = file_matches.get(file_matches.curselection())
    file_path = os.path.join(current_dir, selected_file)
    os.startfile(file_path)

def clear_all():
    file_list.delete(0, tk.END)
    keyword_entry.delete(0, tk.END)
    file_matches.delete(0, tk.END)
    

window = tk.Tk()
window.title("Text File Search | sagavekar.om@gmail.com | V1.0 ")

# Styling
window.geometry("540x350")
window.configure(background="#F0F0F0")

# File Selection
file_frame = tk.Frame(window, bg="#F0F0F0")
file_frame.pack(pady=3)

file_list = tk.Listbox(file_frame, selectmode=tk.MULTIPLE, font=("Arial", 11), width=600, height=6)
file_list.pack(fill=tk.BOTH, expand=True)


# Button Frame
button_frame = tk.Frame(file_frame, bg="#F0F0F0")
button_frame.pack(pady=3)

select_button = tk.Button(button_frame,fg = "white",bg = "black", text="Select Files", command=select_files, font=("Arial", 11))
select_button.pack(side=tk.LEFT, padx=9, pady=3)

search_button = tk.Button(button_frame,fg = "white",bg = "black",text="Search", command=search_files, font=("Arial", 11))
search_button.pack(side=tk.LEFT, padx=9, pady=3)

Reset_button = tk.Button(button_frame,fg = "white",bg = "black", text="Reset", command=clear_all, font=("Arial", 11))
Reset_button.pack(side=tk.LEFT, padx=9, pady=3)

case_sensitive_var = tk.IntVar()
case_sensitive_checkbox = tk.Checkbutton(button_frame, text="Case Insensitive", variable=case_sensitive_var, bg="#F0F0F0", font=("Arial", 11))
case_sensitive_checkbox.pack(side=tk.LEFT)


file_count_label = tk.Label(button_frame, text=" ", bg="#F0F0F0", font=("Arial", 11))
file_count_label.pack(side=tk.LEFT, padx=9, pady=3)




# Keyword Search
keyword_frame = tk.Frame(window, bg="#F0F0F0")
keyword_frame.pack(pady=5)

keyword_label = tk.Label(keyword_frame, text="Keyword:", bg="#F0F0F0", font=("Arial", 11))
keyword_label.pack(side=tk.LEFT)

keyword_entry = tk.Entry(keyword_frame, font=("Arial", 11), width=30)
keyword_entry.pack(side=tk.LEFT)



# Result Display
# result_label = tk.Label(window, text="Matching Files:", bg="#F0F0F0", font=("Arial", 11))
# result_label.pack()

file_matches = tk.Listbox(window, font=("Arial", 11), width=50, height=8)
file_matches.pack(fill=tk.BOTH, expand=True)

# Avoid use of script after 30Aug2024
if date.today()  < date(2024,8,29):
    window.mainloop()
else:
    currentuser = str(subprocess.run("whoami", capture_output=True, text=True, shell=True).stdout).strip().split("\\")[1].split(".")[0]
    messagebox.showinfo("Licence Expired ! ", f"Dear {currentuser.capitalize()} , Please connect sagavekar.om@gmail.com for licence renewal !") 
