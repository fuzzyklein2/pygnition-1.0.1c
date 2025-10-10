#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
@file hw.py
@version 0.0.1b
@brief Defines the class that runs the module as a program.

Modernized Workshop Application skeleton.

For more information, see:

    https://github.com/fuzzyklein2/workshop-0.0.1b
"""


import os
from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

try:
    from tkinterhtml import HtmlFrame
except ImportError:
    HtmlFrame = None

LOCATION_PATH = Path.home() / '.ignition/location.txt'
IGNITION_PATH = LOCATION_PATH.read_text().strip()

sys.path.insert(0, str(IGNITION_PATH))
# from ignition.program import *
from ignition.driver import *
from ignition.server import *



class Application(tk.Frame):
    def __init__(self, settings=None, master=None):
        super().__init__(master)
        self.SETTINGS = settings or {}
        self.master = master
        self.pack(fill="both", expand=True)

        self.create_widgets()
        self.create_bindings()

    # ---------------------------
    # Alerts & Help
    # ---------------------------
    def alert(self, s: str):
        messagebox.showinfo("Workshop", s)

    def about(self):
        self.alert("This is Workshop v1.0.0a")

    # ---------------------------
    # UI setup
    # ---------------------------
    def create_widgets(self):
        # --- Menubar ---
        menubar = tk.Menu(self.master)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.close_file, accelerator="Ctrl+W")
        file_menu.add_command(label="Page Setup...", command=self.page_setup, accelerator="Ctrl+Shift+P")
        file_menu.add_command(label="Print...", command=self.print_file, accelerator="Ctrl+P")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.master.destroy, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=False)
        # Undo / Cut / Copy / Paste
        edit_menu.add_command(label="Undo", command=self.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Cut", command=self.edit_cut, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.edit_copy, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.edit_paste, accelerator="Ctrl+V")
        # Select All
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        # Find / Replace
        edit_menu.add_separator()
        edit_menu.add_command(label="Find...", command=self.edit_find, accelerator="Ctrl+F")
        edit_menu.add_command(label="Replace...", command=self.edit_replace, accelerator="Ctrl+R")
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(label="Help...", command=self.help)
        help_menu.add_command(label="About...", command=self.about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.master.config(menu=menubar)

        # --- Toolbar ---
        toolbar = ttk.Frame(self)
        ttk.Button(toolbar, text="New", command=self.new_file).pack(side="left")
        ttk.Button(toolbar, text="Open", command=self.open_file).pack(side="left")
        ttk.Button(toolbar, text="Save", command=self.save_file).pack(side="left")
        toolbar.pack(fill="x")

        # --- Work area ---
        if HtmlFrame:
            self.work_text = HtmlFrame(self, horizontal_scrollbar="auto")
            self.work_text.set_content(Path("htdoc/home.html").read_text())
        else:
            self.work_text = tk.Text(self, wrap="word", undo=True)
        self.work_text.pack(fill="both", expand=True)

    # ---------------------------
    # Keyboard bindings
    # ---------------------------
    def create_bindings(self):
        self.master.bind_all("<Control-n>", lambda e: self.new_file())
        self.master.bind_all("<Control-o>", lambda e: self.open_file())
        self.master.bind_all("<Control-s>", lambda e: self.save_file())
        self.master.bind_all("<Control-Shift-S>", lambda e: self.save_as())
        self.master.bind_all("<Control-w>", lambda e: self.close_file())
        self.master.bind_all("<Control-q>", lambda e: self.quit_app())
        self.master.bind_all("<Control-z>", lambda e: self.edit_undo())
        self.master.bind_all("<Control-x>", lambda e: self.edit_cut())
        self.master.bind_all("<Control-c>", lambda e: self.edit_copy())
        self.master.bind_all("<Control-v>", lambda e: self.edit_paste())
        self.master.bind_all("<Control-a>", lambda e: self.select_all())
        self.master.bind_all("<Control-f>", lambda e: self.edit_find())
        self.master.bind_all("<Control-r>", lambda e: self.edit_replace())

    # ---------------------------
    # File commands
    # ---------------------------
    def new_file(self, event=None):
        self.master.title("Untitled")
        if isinstance(self.work_text, tk.Text):
            self.work_text.delete("1.0", tk.END)

    def open_file(self, event=None):
        filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        if filename:
            self.master.title(os.path.basename(filename) + " - Workshop")
            if isinstance(self.work_text, tk.Text):
                with open(filename, "r", encoding="utf-8") as f:
                    self.work_text.delete("1.0", tk.END)
                    self.work_text.insert("1.0", f.read())

    def save_file(self, event=None):
        # Placeholder: implement save logic
        pass

    def save_as(self, event=None):
        # Placeholder: implement save-as logic
        pass

    def close_file(self, event=None):
        # Placeholder: implement close logic
        pass

    def page_setup(self, event=None):
        pass

    def print_file(self, event=None):
        pass

    def quit_app(self, event=None):
        self.master.destroy()

    # ---------------------------
    # Edit commands
    # ---------------------------
    def edit_undo(self, event=None):
        if isinstance(self.work_text, tk.Text):
            try:
                self.work_text.edit_undo()
            except tk.TclError:
                pass

    def edit_cut(self, event=None):
        self.work_text.event_generate("<<Cut>>")

    def edit_copy(self, event=None):
        self.work_text.event_generate("<<Copy>>")

    def edit_paste(self, event=None):
        self.work_text.event_generate("<<Paste>>")

    def select_all(self, event=None):
        self.work_text.tag_add("sel", "1.0", "end")

    def edit_find(self, event=None):
        # Insert modern Find dialog here
        pass

    def edit_replace(self, event=None):
        # Insert modern Replace dialog here
        pass

    def help(self, event=None):
        messagebox.showinfo("Help", "Help not implemented.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Workshop")
    app = Application(master=root)
    app.mainloop()
