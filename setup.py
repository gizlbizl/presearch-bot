import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform =="win32":
    base = "Win32GUI"


executables = [Executable("presearch.py", base=base)]
packages = ["pyautogui", "webbrowser", "time"]
excludes = ["tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
        'excludes':excludes,
        'include_files': [
            'config.py',
            'log.txt'
        ],
    },
}
setup(
    name = "BotPresSearch",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)