import os

# Paleta de colores
OBSCURE = '#1c1c1c'
GREEN = '#464E24'
SNOW_WHITE = '#e5e5e5'
BEIGE = '#D8CCB6'
LIGHT_GREY = "#C7C1BC"
DARK_GREY = "#616161"

#ERAS COLOR
DEBUT = "#b9d2b5"
FEARLESS = "#f4cb8d"
SPEAK_NOW = "#d1b2d2"
RED = "#823549"
I998 = "b5e9f6"

ERAS_COLOR = {
    DEBUT : "#b9d2b5",
    FEARLESS : "#f4cb8d",
    SPEAK_NOW : "#d1b2d2",
    RED : "#823549",
    I998 : "b5e9f6"
}

# Ruta de la fuente
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Sube un nivel desde 'config'
FONT_PATH = os.path.join(BASE_DIR, 'fonts', 'IMFellDWPica-Regular.ttf')
FONT_SIZE = 12  # Ajusta el tamaño de la fuente según sea necesario


def center_windows(ventana,app_width,app_height):
    window_width = ventana.winfo_screenwidth()
    window_height = ventana.winfo_screenheight()
    x = int((window_width / 2) - (app_width / 2))
    y = int((window_height / 2) - (app_height / 2 ))
    return ventana.geometry(f"{app_width}x{app_height}+{x}+{y}")

