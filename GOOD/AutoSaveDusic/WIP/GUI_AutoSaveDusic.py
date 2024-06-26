import tkinter as tk
from tkinter import filedialog

My_Font_Size = 16


def choose_folder():
    global Dir_Output_Folder
    Dir_Output_Folder = filedialog.askdirectory()
    if Dir_Output_Folder:
        print(f"Dir_Output_Folder: {Dir_Output_Folder}")
        folder_label.config(
            text=f"This is where your music will be exported to:\n{Dir_Output_Folder}")


def choose_parent_folder():
    global Dir_Parent_FLP_Folder
    Dir_Parent_FLP_Folder = filedialog.askdirectory()
    if Dir_Parent_FLP_Folder:
        print(f"Dir Parent FLP Folder: {Dir_Parent_FLP_Folder}")
        parent_folder_label.config(
            text=f"This is the top directory where all your FLP projects are located:\n{Dir_Parent_FLP_Folder}")


def continue_button_click():
    # Add your continuation logic here
    print("Continue button clicked")
    with open("Init_Data.txt", "w") as file:
        file.write(f"Dir_Output_Folder = {Dir_Output_Folder}\n")
        file.write(f"parent_folder_path = {Dir_Parent_FLP_Folder}")


root = tk.Tk()
root.title("AutoSaveDusic Settings")

# Get the screen width
screen_width = root.winfo_screenwidth()

# Set the default window size to be half the screen width
default_width = screen_width // 2
default_height = 400
root.geometry(f"{default_width}x{default_height}")

# Make the window non-resizable
root.resizable(False, False)

output_folder_button = tk.Button(
    root, text="Output Folder", command=choose_folder, font=("Arial", My_Font_Size))
output_folder_button.pack(anchor="w", pady=(10, 0), padx=10)

folder_label = tk.Label(root, text="This is where your music will be exported to:\nExample: C:/Documents/Music/FLP Songs",
                        anchor="w", justify=tk.LEFT, font=("Arial", My_Font_Size), wraplength=default_width - 20, highlightthickness=1, takefocus=True)
folder_label.pack(fill="x", padx=10)

parent_flp_button = tk.Button(root, text="Parent FLP Project Folder",
                              command=choose_parent_folder, font=("Arial", My_Font_Size))
parent_flp_button.pack(anchor="w", pady=(50, 0), padx=10)

parent_folder_label = tk.Label(root, text="This is the top directory where all your FLP projects are located:\nExample: C:/Users/UserName/Documents/Image-Line/FL Studio/Projects/FL 20 - projects",
                               anchor="w", justify=tk.LEFT, font=("Arial", My_Font_Size), wraplength=default_width - 20, highlightthickness=1, takefocus=True)
parent_folder_label.pack(fill="x", padx=10)

continue_button = tk.Button(
    root, text="Submit", command=continue_button_click, font=("Arial", My_Font_Size))
continue_button.pack(side=tk.BOTTOM, pady=(20, 10), padx=10, anchor="e")

root.mainloop()