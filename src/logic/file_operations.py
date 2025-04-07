# src/logic/file_operations.py
import os
import shutil
from tkinter import messagebox as MessageBox

def guardar_datos(carpeta_referencia, carpeta_archivos, carpeta_destino, progress_bar=None):
    # Verificar si las carpetas son válidas
    if not (os.path.isdir(carpeta_referencia) and os.path.isdir(carpeta_archivos) and os.path.isdir(carpeta_destino)):
        MessageBox.showerror(title='Error', message='Ingrese rutas válidas')
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

    # Configurar la barra de progreso si está disponible
    if progress_bar:
        progress_bar.set(0)

    # Mover los archivos encontrados a la carpeta de destino
    moved_count = 0
    for i, archivo in enumerate(archivos_a_mover, 1):
        origen = os.path.join(carpeta_archivos, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        try:
            shutil.move(origen, destino)
            moved_count += 1
            # Actualizar la barra de progreso si está disponible
            if progress_bar:
                progress_bar.set(i / num_archivos_a_mover)
        except Exception as e:
            print(f"No se pudo mover el archivo {archivo}: {e}")

    MessageBox.showinfo(title='Operación Completada', message=f'Se han trasladado {moved_count} archivos.')