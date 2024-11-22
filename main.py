import tkinter as tk
from tkinter import filedialog, messagebox
from text_operations import cut, copy, paste
from file_operations import new_file, save_file, open_file
from about import show_about

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.root.geometry("600x400")
        
        self.filename = None
        
        # Criando a barra de menus
        self.create_menu()
        
        # Caixa de texto
        self.textbox = tk.Text(self.root, wrap='word')
        self.textbox.pack(expand=True, fill='both')

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # Menu Arquivo
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        
        # Menu Editar
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Recortar", command=self.cut)
        edit_menu.add_command(label="Copiar", command=self.copy)
        edit_menu.add_command(label="Colar", command=self.paste)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        
        # Menu Ferramentas
        menubar.add_cascade(label="Ferramentas")
        
        # Menu Ajuda
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Sobre", command=self.show_about)
        menubar.add_cascade(label="Ajuda", menu=help_menu)

        self.root.config(menu=menubar)

    def new_file(self):
        self.filename = None
        self.textbox.delete(1.0, tk.END)
        self.update_title()

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if self.filename:
            save_file(self.filename, self.textbox.get(1.0, tk.END))
            self.update_title()

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if self.filename:
            content = open_file(self.filename)
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, content)
            self.update_title()

    def update_title(self):
        if self.filename:
            self.root.title(f"Bloco de Notas - {self.filename}")
        else:
            self.root.title("Bloco de Notas")
    
    def cut(self):
        cut(self.textbox)
    
    def copy(self):
        copy(self.textbox)
    
    def paste(self):
        paste(self.textbox)
    
    def show_about(self):
        show_about(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
