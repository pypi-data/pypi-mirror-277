from PyWebUI.Constants import *
from PyWebUI import Globals
from PyWebUI.utilities import util4string as u4s
from PyWebUI.utilities import util4code as u4c
Launcher = None

def build(project_name: str, main_html: str, window_size: tuple) -> None:
    global Launcher
    Globals.app_config.project_name = project_name
    Globals.app_config.main_html = main_html
    Globals.app_config.ip = 'localhost'
    Globals.app_config.port = 1234
    Globals.app_config.window_size = window_size
    app_build = None # Initialization only

    if PLATFORM=='Windows':
        def app_build():
            global Launcher
            from PyWebUI import Launcher_windows 
            
            Launcher = Launcher_windows.App()
    else:
        def app_build():
            global Launcher
            from PyWebUI import Launcher_android
            Launcher = Launcher_android.app

    app_build()
    
    return

def run_loop():
    Launcher.run()