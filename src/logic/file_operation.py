# src/logic/file_operations.py
import os
import shutil
from tkinter import messagebox as MessageBox
from customtkinter import CTkProgressBar # Si aún necesitas esta importación

def guardar_datos(carpeta_referencia, carpeta_archivos, carpeta_destino):
    # Verificar si las carpetas son válidas
    if not (os.path.isdir(carpeta_referencia) and os.path.isdir(carpeta_archivos) and os.path.isdir(carpeta_destino)):
        MessageBox.showerror(title='Error', message='Ingrese rutas válidas') # Usar mensaje de error
        return

    # Obtener la lista de referencia (nombres de archivos)
    lista_referencia = set(os.listdir(carpeta_referencia))

    # Obtener los archivos en la segunda carpeta
    archivos_en_carpeta2 = os.listdir(carpeta_archivos)

    # Filtrar los archivos en la segunda carpeta que coincidan con la referencia
    archivos_a_mover = [archivo for archivo in archivos_en_carpeta2 if archivo in lista_referencia]

    num_archivos_a_mover = len(archivos_a_mover)
    if num_archivos_a_mover == 0:
        MessageBox.showinfo(title='Información', message='No se encontraron archivos para mover.')
        return

    # Mover los archivos encontrados a la carpeta de destino
    moved_count = 0
    for archivo in archivos_a_mover:
        origen = os.path.join(carpeta_archivos, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        try:
            shutil.move(origen, destino)
            moved_count += 1
        except Exception as e:
            print(f"No se pudo mover el archivo {archivo}: {e}")

    MessageBox.showinfo(title='Operación Completada', message=f'Se han trasladado {moved_count} archivos.')