from tkinter import *
import tkinter.messagebox
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile, asksaveasfile
import os
import scanner
import cv2


# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("400x200")
win.config(bg='#808080')


def open_file():
    file = filedialog.askopenfile(
        mode='r', filetypes=[('Image Files', '*.jpg'), ('Image Files', '*.jpeg')])
    if file:
        filepath = os.path.abspath(file.name)
        global image
        image = scanner.scan(filepath)
        cv2.imshow("Scanned", cv2.resize(image, (600, 800)))


def save_file():
    files = [('Image Files', '*.jpg*'),
             ('Image Files', '*.jpeg')]
    try:
        file = asksaveasfile(filetypes=files, defaultextension=files)
        cv2.imwrite(file.name, image)
    except:
        tkinter.messagebox.showerror(message="Sorry! something went wrong!")


# Add a Label widget
label = Label(win, text="Document Scanner",
              font=('Georgia 13'))
label.pack(pady=10)

# Buttons
ttk.Button(win, text="Open JPG/JPEG",
           command=open_file, width=20).pack(pady=10)
btn = ttk.Button(win, text='Save JPG/JPEG',
                 command=lambda: save_file(), width=20)
btn.pack(side=TOP, pady=10)
ttk.Button(win, text="Quit", command=quit).pack(pady=10)

if __name__ == '__main__':
    win.mainloop()
