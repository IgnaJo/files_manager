# src/logic/file_operations.py
import os
import shutil
from tkinter import messagebox as MessageBox

def guardar_datos(carpeta_referencia, carpeta_archivos, carpeta_destino, copy_mode=False):
    # Verificar si las carpetas son válidas
    if not (os.path.isdir(carpeta_referencia) and os.path.isdir(carpeta_archivos) and os.path.isdir(carpeta_destino)):
        MessageBox.showerror(title='Error', message='Ingrese rutas válidas')
        return

    # Obtener la lista de referencia (nombres de archivos)
    lista_referencia = set(os.listdir(carpeta_referencia))

    # Obtener los archivos en la segunda carpeta
    archivos_en_carpeta2 = os.listdir(carpeta_archivos)

    # Filtrar los archivos en la segunda carpeta que coincidan con la referencia
    archivos_a_procesar = [archivo for archivo in archivos_en_carpeta2 if archivo in lista_referencia]

    num_archivos = len(archivos_a_procesar)
    if num_archivos == 0:
        MessageBox.showinfo(title='Información', message='No se encontraron archivos para procesar.')
        return

    # Copiar o mover los archivos encontrados a la carpeta de destino
    processed_count = 0
    operation = shutil.copy2 if copy_mode else shutil.move
    operation_name = "copiado" if copy_mode else "movido"

    for archivo in archivos_a_procesar:
        origen = os.path.join(carpeta_archivos, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        try:
            operation(origen, destino)
            processed_count += 1
        except Exception as e:
            print(f"No se pudo {operation_name} el archivo {archivo}: {e}")

    MessageBox.showinfo(
        title='Operación Completada', 
        message=f'Se han {operation_name} {processed_count} archivos.'
    )