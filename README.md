
# Gestor de Archivos 
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
- Ms Build Tools 2019 - 

## Instalación
- Clonar repositorio: `git clone https://github.com/IgnaJo/files_manager.git`
- Activar Entorno Virtual: ` source env_fm/bin/activate` 
- Instalar tkinterdnd2: `pip install tkinterdnd2`
- Instalar CustomTkinter: `pip install customtkinter`

## Packaging
- Instalar Auto Py to Exe: `pip install auto-py-to-exe`
- Ejecutar: `auto-py-to-exe`
- pyinstaller --noconfirm --onedir --windowed --icon "assets/images/logo.ico" --add-data "C:\Users\Jose Ignacio\Desktop\WorkSpace\files_manager\files_manager\venv\Lib\site-packages\tkinterdnd2;tkinterdnd2/" --add-data "C:\Users\Jose Ignacio\Desktop\WorkSpace\files_manager\files_manager\venv\Lib\site-packages\customtkinter;customtkinter/" "C:\Users\Jose Ignacio\Desktop\WorkSpace\files_manager\files_manager\drag_app.py"

