from tkinter import filedialog

def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def new_file(textbox):
    textbox.delete(1.0, 'end')
