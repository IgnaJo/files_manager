# Files Manager

A Python GUI application for organizing files based on a reference folder.

## Prerequisites

- Python 3.x
- Terminal/Command Prompt

## First Time Setup

1. Clone or download the project to your local machine

2. Open a terminal and navigate to the project directory:
```bash
cd path/to/files_manager
```

3. Create a virtual environment:
```bash
python3 -m venv env_fm
```

4. Activate the virtual environment:
- On macOS/Linux:
```bash
source env_fm/bin/activate
```
- On Windows:
```bash
env_fm\Scripts\activate
```

5. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated (see step 4 above)

2. Run the application:
```bash
python drag_app.py
```

## How to Use

1. The application window will open with three input fields:
   - Reference folder: Contains the list of file names to match
   - Source folder: Contains the files you want to move
   - Destination folder: Where matched files will be moved to

2. You can input folder paths by:
   - Typing the path directly
   - Dragging and dropping folders from your file explorer

3. Click "Mover Archivos" to start moving files
   - Only files from the source folder that match names in the reference folder will be moved
   - A progress bar will show the operation's progress

4. Click "Limpiar Campos" to clear all fields

## Dependencies

- customtkinter==5.2.2
- tkinterdnd2==0.4.2
