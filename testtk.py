import tkinter as tk
import tkinter.filedialog as fd
from PyPDF2 import PdfMerger
import shutil
import os

merger = PdfMerger()
window = tk.Tk()
window.title("First TK window")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("700x500")
label = tk.Label(window, text="Click me", font='Calibri 15 bold')
label.pack(pady=20)
path_to_files=r'incoming/'

# Function to update the label text for first button click in Tkinter
def on_click_btn1():
    label["text"] = "You clicked first button"

# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "You clicked second button"

pdf_files_list=[]

def open_file():
   file = fd.askopenfilenames(parent=window, title='Choose a File')
   pdf_files_list=list((window.splitlist(file)))
   for x in range(len(pdf_files_list)):
       shutil.copy(pdf_files_list[x],path_to_files)

def merge_files():
    print(len(pdf_files_list))
    # Get the file names in the directory
    for root, dirs, file_names in os.walk(path_to_files):
        # Iterate over the list of the file names
        for file_name in file_names:
            # Append PDF files
            merger.append(path_to_files + file_name)
    file_name =textbox.get() + ".pdf"
    merger.write(file_name)
    merger.close()
    for f in os.listdir(path_to_files):
        os.remove(os.path.join(path_to_files, f))
    close_window()

def close_window():
    window.destroy()

btn0=tk.Button(window, text="Select your files", command=open_file)
btn0.pack(pady=20)

textbox = tk.Entry(window,textvariable="Rename merged file as")
textbox.pack(pady=20)

merge_btn = tk.Button(window, text="Merge", command=merge_files)
merge_btn.pack(pady=20)

window.mainloop()