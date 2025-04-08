# src/gui/app_window.py
import os
import sys
from tkinterdnd2 import DND_FILES, TkinterDnD
from customtkinter import *
import tkinter.font as tkFont
from tkinter import messagebox as MessageBox
import assets.config.config
from assets.config.config import FONT_PATH, FONT_SIZE, OBSCURE, GREEN, LIGHT_GREY, ERAS_COLOR, RED, DEBUT, DARK_GREY
from logic.file_operation import guardar_datos
from tkinterdnd2 import TkinterDnD


def get_tkdnd_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (pyinstaller)
        base_path = sys._MEIPASS
        tkdnd_path = os.path.join(base_path, 'tkdnd2.8')
        if os.path.exists(tkdnd_path):
            return tkdnd_path
    return None

class MainWindow(TkinterDnD.Tk):
    def __init__(self):
        os.environ['TCLLIBPATH'] = os.path.abspath("tkdnd2.8")
        # Initialize tkdnd path for Windows
        tkdnd_path = get_tkdnd_path()
        if tkdnd_path:
            os.environ['TKDND_LIBRARY'] = tkdnd_path

        super().__init__()
        set_appearance_mode("Dark")
        set_default_color_theme("blue")
        self.title("Gestor de Archivos")
        w, h = 800, 380
        self.resizable(0, 0)
        
        # Handle icon path for both development and bundled versions
        icon_path = 'assets/images/logo.ico'
        if getattr(sys, 'frozen', False):
            # Running in a bundle
            icon_path = os.path.join(sys._MEIPASS, icon_path)
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
            
        assets.config.config.center_windows(self, w, h)

        self.form_frame = CTkFrame(self)
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.8)

        self.label_instrucciones = CTkLabel(self.form_frame, text="Traslada tus Archivos :", font=("Segoe UI BLACK",22))
        self.label_instrucciones.grid(row=0, column=0, columnspan=2, pady=10)

        font_label = "Segoe UI Semibold"

        self.label_folder_reference = CTkLabel(self.form_frame, text="Carpeta de referencia :", font=(font_label, 16), padx=5)
        self.label_folder_reference.grid(row=1, column=0, padx=5, sticky="w")

        self.label_folder1 = CTkLabel(self.form_frame, text="Carpeta con archivos a mover", font=(font_label, 16), padx=5)
        self.label_folder1.grid(row=2, column=0, padx=5, sticky="w")

        self.label_folder2 = CTkLabel(self.form_frame, text="Carpeta de destino :", font=(font_label, 16), padx=5)
        self.label_folder2.grid(row=3, column=0, padx=5, sticky="w")

        self.label_error_ruta = CTkLabel(self.form_frame, text="Ingrese una ruta válida",  text_color="red")

        self.entry1 = CTkEntry(self.form_frame, width=450)
        self.entry1.grid(row=1, column=1, pady=5, padx=5)

        self.entry2 = CTkEntry(self.form_frame, width=450)
        self.entry2.grid(row=2, column=1, pady=5, padx=5)

        self.entry3 = CTkEntry(self.form_frame, width=450)
        self.entry3.grid(row=3, column=1, pady=5, padx=5)

        self.progress_var = StringVar()
        self.progress_bar = CTkProgressBar(self.form_frame, width=400, mode='determinate')
        self.progress_bar.grid(row=5, column=0, columnspan=2, pady=10)

        # Add checkbox for copy mode
        self.copy_mode_var = BooleanVar(value=False)
        self.copy_mode_checkbox = CTkCheckBox(
            self.form_frame, 
            text="Copiar archivos (en lugar de moverlos)", 
            variable=self.copy_mode_var,
            font=(font_label, 14),
            width=600,  
            height=30   
        )
        self.copy_mode_checkbox.grid(
            row=6, 
            column=0, 
            columnspan=2, 
            pady=(15, 5),  
            sticky="w", 
            padx=20  
        )

        self.button_guardar = CTkButton(self.form_frame, text="Mover Archivos", font=(font_label, 16), text_color=OBSCURE, fg_color=LIGHT_GREY, hover_color=DEBUT, anchor="center", command=self.iniciar_movimiento) # Llama a un método
        self.button_guardar.grid(row=4, column=0, padx=5, pady=10, sticky="ew")

        self.button_clean_entry = CTkButton(self.form_frame, text="Limpiar Campos", font=(font_label, 16), text_color=OBSCURE, fg_color=LIGHT_GREY, hover_color=RED, anchor="center", command=self.clean_entries)
        self.button_clean_entry.grid(row=4, column=1, padx=5, pady=10, sticky="ew")

        self.form_frame.grid_columnconfigure(0, weight=1, minsize=100)
        self.form_frame.grid_columnconfigure(1, weight=1, minsize=100)

        self.drop_target_register(DND_FILES)
        self.entry1.drop_target_register(DND_FILES)
        self.entry1.dnd_bind('<<Drop>>', lambda event: self.drop(event, self.entry1))
        self.entry2.drop_target_register(DND_FILES)
        self.entry2.dnd_bind('<<Drop>>', lambda event: self.drop(event, self.entry2))
        self.entry3.drop_target_register(DND_FILES)
        self.entry3.dnd_bind('<<Drop>>', lambda event: self.drop(event, self.entry3))

    def clean_entries(self):
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.delete(0, "end")
        self.progress_var.set('')
        self.progress_bar.set(0)
        if hasattr(self, 'label_error_ruta') and self.label_error_ruta.winfo_ismapped():
            self.label_error_ruta.grid_forget()

    def drop(self, event, entry):
        entry.delete(0, "end")
        path = event.data.strip('{}')
        entry.insert(0, path)

    def iniciar_movimiento(self):
        carpeta_referencia = self.entry1.get()
        carpeta_archivos = self.entry2.get()
        carpeta_destino = self.entry3.get()

        # Validación básica del lado del cliente (opcional, pero buena práctica)
        if not (carpeta_referencia and carpeta_archivos and carpeta_destino):
            MessageBox.showerror(title='Error', message='Por favor, complete todos los campos.')
            return

        # Llama a la función de lógica desde file_operations
        guardar_datos(
            carpeta_referencia, 
            carpeta_archivos, 
            carpeta_destino,
            copy_mode=self.copy_mode_var.get()
        )
        self.clean_entries() # Limpia los campos después de la operación

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()