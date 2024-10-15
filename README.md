
# Gestor de Archivos 
<img width="791" alt="image" src="https://github.com/user-attachments/assets/f1dbe20c-a057-47e6-8785-f79a9d5df42f">

## Descripción
La aplicación es una herramienta de escritorio desarrollada con Tkinter que permite a los usuarios gestionar archivos por medio de una interfaz gráfica de arrastrar y soltar carpetas. El principal objetico es agilizar la reorganizacion de documentos firmados digitalmente, devolviendolos a la estructura original de carpetas, las cuales se identifican por fecha.

## Características principales:
- Organización automática de documentos: La app permite que los documentos, una vez firmados y descargados en una única carpeta, sean reubicados en su estructura original de carpetas basada en la fecha.
- Interfaz intuitiva: Utiliza una interfaz de usuario sencilla y amigable con soporte para arrastrar y soltar archivos, gracias a tkinterdnd2.
- Personalización visual: La aplicación incorpora customtkinter para un diseño visual atractivo y personalizable.
- Agilización del flujo de trabajo: Optimiza el proceso de manejo de documentos, especialmente útil en oficinas donde se requiere un firmador electrónico.

## Tecnologías utilizadas
- Python
- Tkinterdnd2
- CustomTkinter
- Ms Build Tools 2019 - 2024

## Instalación
- Clonar repositorio: `git clone https://github.com/IgnaJo/files_manager.git`
- Activar Entorno Virtual: ` source venv/bin/activate` 
- Instalar tkinterdnd2: `pip install tkinterdnd2`
- Instalar CustomTkinter: `pip install customtkinter`

## Packaging
- Instalar Auto Py to Exe: `pip install auto-py-to-exe`
- Ejecutar auto-py añadiendo los directorios de logo.ico, TkinderDnd2 y CustomTkinter: `auto-py-to-exe`
- Comando de de packaging : `pyinstaller --noconfirm --onedir --windowed --icon "assets/images/logo.ico" --add-data "C:\Users\<your user>\<your folder>\files_manager\files_manager\venv\Lib\site-packages\tkinterdnd2;tkinterdnd2/" --add-data "C:\Users\<your user>\<your folder>\files_manager\files_manager\venv\Lib\site-packages\customtkinter;customtkinter/" "C:\Users\<your user>\<your folder>\files_manager\files_manager\drag_app.py"`

## Consideraciones
- Aveces el ejecutable puede tener problemas con el logo y producir el siguiente error:
   <img width="391" alt="image" src="https://github.com/user-attachments/assets/11c9d36e-0cba-41da-9b4f-782344b2ad8f">
- Para solucionar se debe agregar manualmente la carpeta "assets" en `dist/_interal/`
  
  <img width="236" alt="image" src="https://github.com/user-attachments/assets/6cecf0df-9252-481c-b451-55c5d26dcbdb">



