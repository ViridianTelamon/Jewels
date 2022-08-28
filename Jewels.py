"""    
    Copyright (C) 2022 ViridianTelamon (Viridian)
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

print("Jewels | Text Editor")

print("\nBy:  ViridianTelamon")

root = Tk()
root.title("Jewels Text Editor | By:  ViridianTelamon")
root.geometry("800x600")

global open_status_name
open_status_name = False

global selected
selected = False


def new_file():
    text.delete("1.0", END)
    root.title("New File | Jewels Text Editor | By:  ViridianTelamon")
    status_bar.config(text="New File")

    global open_status_name
    open_status_name = False

def open_file():
    text.delete("1.0", END)

    text_file = filedialog.askopenfilename(initialdir="", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    
    if text_file:
        global open_status_name
        open_status_name = text_file

    name = text_file
    status_bar.config(text=f"{name}")
    root.title(f"{name} | Jewels Text Editor | By:  ViridianTelamon")

    text_file = open(text_file, "r")
    text_file_open = text_file.read()
    text.insert(END, text_file_open)
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="", title="Save As", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f"Saved:  {name}")
        #name = name.replace("C:/", "")
        #root.title("Jewels Text Editor | By:  ViridianTelamon")    
        root.title(f"{name} | Jewels Text Editor | By:  ViridianTelamon")

    text_file = open(text_file, "w")
    text_file.write(text.get(1.0, END))
    text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, "w")
        text_file.write(text.get(1.0, END))
        text_file.close()
        status_bar.config(text="File Saved")
    else:
        save_as_file()

def cut_text(e):
    global selected

    if e:
        selected = root.clipboard_get
    else:
        if text.selection_get():
            selected = text.selection_get()
            text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text(e):
    global selected

    if e:
        selected = root.clipboard_get

    if text.selection_get():
        selected = text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text(e):
    global selected

    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = text.index(INSERT)
            text.insert(position, selected)

def bold_text():
    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")

    text.tag_configure("bold", font=bold_font)

    current_tags = text.tag_names("sel.first")

    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")

def italics_text():
    italics_font = font.Font(text, text.cget("font"))
    italics_font.configure(slant="italic")

    text.tag_configure("italics", font=italics_font)

    current_tags = text.tag_names("sel.first")

    if "italics" in current_tags:
        text.tag_remove("italics", "sel.first", "sel.last")
    else:
        text.tag_add("italics", "sel.first", "sel.last")

def underline_text():
    underline_font = font.Font(text, text.cget("font"))
    underline_font.configure(underline=True)

    text.tag_configure("underline", font=underline_font)

    current_tags = text.tag_names("sel.first")

    if "underline" in current_tags:
        text.tag_remove("underline", "sel.first", "sel.last")
    else:
        text.tag_add("underline", "sel.first", "sel.last")

def colour_text():
    colours = colorchooser.askcolor()[1]

    if colours:
        status_bar.config(text=f"{colours}")

        colour_font = font.Font(text, text.cget("font"))

        text.tag_configure("colour", font=colour_font, foreground=colours)

        current_tags = text.tag_names("sel.first")

        if "colour" in current_tags:
            text.tag_remove("colour", "sel.first", "sel.last")
        else:
            text.tag_add("colour", "sel.first", "sel.last")


frame = Frame(root)
frame.pack(pady=5)

text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

horizontal_scroll = Scrollbar(frame, orient="horizontal")
horizontal_scroll.pack(side=BOTTOM, fill=X)

text = Text(frame, width=97, height=25, font=("Helvetica", 16), selectbackground="skyblue", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=horizontal_scroll.set)
text.pack(pady=5)

text_scroll.config(command=text.yview)
horizontal_scroll.config(command=text.xview)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_separator()
edit_menu.add_command(label="Redo", command=text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=lambda: copy_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: cut_text(False))

text_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Text", menu=text_menu)
text_menu.add_command(label="Bold", command=bold_text)
text_menu.add_separator()
text_menu.add_command(label="Italic", command=italics_text)
text_menu.add_separator()
text_menu.add_command(label="Underline", command=underline_text)
text_menu.add_separator()
text_menu.add_command(label="Colour", command=colour_text)

status_bar = Label(root, text="Ready          ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

root.bind("<Control-Key-X>", cut_text)
root.bind("<Control-Key-C>", copy_text)
root.bind("<Control-Key-V>", paste_text)

root.mainloop()
