import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

def show_progress_bar(total_size):
    root = tk.Tk()
    root.title("Téléchargement en cours")
    progress = tk.ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", maximum=total_size)
    progress.pack(pady=10)
    return progress

