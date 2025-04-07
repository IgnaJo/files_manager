# src/logic/file_operations.py
import os
import shutil
from tkinter import messagebox as MessageBox

def guardar_datos(carpeta_referencia, carpeta_archivos, carpeta_destino, progress_bar=None, is_copy=False):
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

    # Copiar o mover los archivos encontrados a la carpeta de destino
    moved_count = 0
    operation_func = shutil.copy2 if is_copy else shutil.move
    operation_type = "copiado" if is_copy else "movido"

    for i, archivo in enumerate(archivos_a_mover, 1):
        origen = os.path.join(carpeta_archivos, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        try:
            operation_func(origen, destino)
            moved_count += 1
            # Actualizar la barra de progreso si está disponible
            if progress_bar:
                progress_bar.set(i / num_archivos_a_mover)
        except Exception as e:
            print(f"No se pudo {operation_type} el archivo {archivo}: {e}")

    MessageBox.showinfo(title='Operación Completada', message=f'Se han {operation_type} {moved_count} archivos.')