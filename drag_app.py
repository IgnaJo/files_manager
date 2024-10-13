import os
import shutil
from tkinterdnd2 import DND_FILES, TkinterDnD
from customtkinter import *

import assets.config.config
from assets.config.config import FONT_PATH, FONT_SIZE, OBSCURE, GREEN, LIGHT_GREY, ERAS_COLOR, RED, DEBUT, DARK_GREY
import tkinter.font as tkFont
from tkinter import messagebox as MessageBox


# Configurar la ventana principal usando TkinterDnD y customtkinter
ventana = TkinterDnD.Tk()  # Usamos Tk para la funcionalidad de arrastrar y soltar
set_appearance_mode("Dark")  # Ajuste de tema claro/oscuro para customtkinter
set_default_color_theme("blue")  # Tema de colores predeterminado de customtkinter
ventana.title("Gestor de Archivos")
w, h = 800, 320
ventana.resizable(0, 0)
ventana.iconbitmap('assets/images/logo.ico')
#ventana.configure(bg=LIGHT_GREY)
assets.config.config.center_windows(ventana, w, h)



# Crear un frame para centrar los elementos del formulario
form_frame = CTkFrame(ventana)
form_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.8)
  # Centrar el frame

# Etiqueta de instrucciones
label_instrucciones = CTkLabel(
    form_frame, text="Traslada tus Archivos :", font=("Segoe UI BLACK",22),

)
label_instrucciones.grid(row=0, column=0, columnspan=2, pady=10)

font_label = "Segoe UI Semibold"

# Etiquetas para cada entrada
label_folder_reference = CTkLabel(
    form_frame, text="Carpeta de referencia :",
    font=(font_label, 16),
    padx=5
)
label_folder_reference.grid(row=1, column=0, padx=5, sticky="w")

label_folder1 = CTkLabel(
    form_frame,
    text="Carpeta con archivos a mover",
    font=(font_label, 16),
    padx=5
)
label_folder1.grid(row=2, column=0, padx=5, sticky="w")

label_folder2 = CTkLabel(
    form_frame,
    text="Carpeta de destino :",
    font=(font_label, 16),
    padx=5
)
label_folder2.grid(row=3, column=0, padx=5, sticky="w")

label_error_ruta = CTkLabel(
    form_frame, text="Ingrese una ruta válida",  text_color="red"
)

# Crear entradas para mostrar las rutas de las carpetas
entry1 = CTkEntry(form_frame, width=450,)
entry1.grid(row=1, column=1, pady=5, padx=5)

entry2 = CTkEntry(form_frame, width=450)
entry2.grid(row=2, column=1, pady=5, padx=5)

entry3 = CTkEntry(form_frame, width=450)
entry3.grid(row=3, column=1, pady=5, padx=5)

# Crear la barra de progreso
progress_var = StringVar()
progress_bar = CTkProgressBar(
    form_frame, width=400, mode='determinate'
)
progress_bar.grid(row=5, column=0, columnspan=2, pady=10)


# Función para limpiar las entradas
def clean_entries():
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    progress_var.set('')  # Resetea el texto de la barra de progreso
    progress_bar.set(0)  # Resetea la barra de progreso


# Función para guardar los valores de los campos de entrada
def guardar_datos():
    carpeta_referencia = entry1.get()
    carpeta_archivos = entry2.get()
    carpeta_destino = entry3.get()

    # Verificar si las carpetas son válidas
    if not (os.path.isdir(carpeta_referencia) and os.path.isdir(carpeta_archivos) and os.path.isdir(carpeta_destino)):
        label_error_ruta.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        return

    # Obtener la lista de referencia (nombres de archivos)
    lista_referencia = set(os.listdir(carpeta_referencia))

    # Obtener los archivos en la segunda carpeta
    archivos_en_carpeta2 = os.listdir(carpeta_archivos)

    # Filtrar los archivos en la segunda carpeta que coincidan con la referencia
    archivos_a_mover = [archivo for archivo in archivos_en_carpeta2 if archivo in lista_referencia]

    # Establecer la longitud máxima de la barra de progreso
    progress_bar.configure(maximum=len(archivos_a_mover))
    progress_bar.set(0)

    # Mover los archivos encontrados a la carpeta de destino
    for i, archivo in enumerate(archivos_a_mover, start=1):
        origen = os.path.join(carpeta_archivos, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        try:
            shutil.move(origen, destino)
        except Exception as e:
            print(f"No se pudo mover el archivo {archivo}: {e}")

        # Actualizar la barra de progreso
        progress_bar.set(i / len(archivos_a_mover))
        ventana.update_idletasks()  # Refrescar la interfaz

    clean_entries()
    MessageBox.showinfo(title='Operación Completada', message=f'Se han trasladado {i} Archivos')


# Crear el botón para guardar los valores de las entradas y mover archivos
button_guardar = CTkButton(
    form_frame,
    text="Mover Archivos",
    font=(font_label, 16),
    text_color=OBSCURE,
    fg_color=LIGHT_GREY,
    hover_color=DEBUT,
    anchor="center",
    command=guardar_datos
)
button_guardar.grid(row=4, column=0, padx=5, pady=10, sticky="ew")

# Crear el botón para limpiar las entradas
button_clean_entry = CTkButton(
    form_frame,
    text="Limpiar Campos",
    font=(font_label, 16),
    text_color=OBSCURE,
    fg_color=LIGHT_GREY,
    hover_color=RED,
    anchor="center",
    command=clean_entries
)
button_clean_entry.grid(row=4, column=1, padx=5, pady=10, sticky="ew")

# Ajustar las columnas del frame para centrar los botones y permitirles expansión
form_frame.grid_columnconfigure(0, weight=1, minsize=100)  # Controlar el tamaño mínimo
form_frame.grid_columnconfigure(1, weight=1, minsize=100)





# Función que se ejecuta cuando se arrastra una carpeta a la ventana
def drop(event, entry):
    entry.delete(0, "end")
    entry.insert(0, event.data)


# Habilitar las entradas para aceptar archivos/carpetas arrastrados
ventana.drop_target_register(DND_FILES)

# Asociar la acción de arrastrar y soltar con la función 'drop' para cada entrada
entry1.drop_target_register(DND_FILES)
entry1.dnd_bind('<<Drop>>', lambda event: drop(event, entry1))

entry2.drop_target_register(DND_FILES)
entry2.dnd_bind('<<Drop>>', lambda event: drop(event, entry2))

entry3.drop_target_register(DND_FILES)
entry3.dnd_bind('<<Drop>>', lambda event: drop(event, entry3))

# Iniciar la ventana
ventana.mainloop()
