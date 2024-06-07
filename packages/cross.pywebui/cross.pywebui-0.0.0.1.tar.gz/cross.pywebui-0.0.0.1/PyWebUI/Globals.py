"""
This script consists of functions/class/variables that are shared by the whole application.
Many variables are only instantiated, to be assigned by other scripts;
    To access values across multiple scripts while avoiding circular imports.
"""
from PyWebUI.utilities import \
    util4string as u4s, \
    util4code as u4c
import threading

class Flags:
    """
    Contains flags; variables that interacts with multiple scripts and can change.
    Does not need to be instantiated.
    """
    class Launcher:
        # 1 time use; becomes true if connection has been established with the frontend. Shared by Frontend and Launchers
        frontend_connected = False

class FrontEndAPI:
    """
    Initialization; is given methods by Frontend script.
        Contains functions that can be used by user defined scripts.
    """
    def __init__(self):
        pass

class Config:
    """
    Initialization; is given properties during App initialization
    """
    def __init__(self):
        pass

class FrontEndSocket:
    """
    Initialization; is instantiated from Launcher.
    Class for controlling the frontend socket from Frontend.
    A 2 way communication.
    """
    def __init__(self, server):
        self.socket = None
        self.server = server
    def create(self):
        self.socket = threading.Thread(target = lambda *args: self.server.start_server())
        self.socket.start()
    def restart(self):
        try:
            self.socket.close()
            self.create()
        except Exception as e:
            pass

# Instantiations
app_config = Config()
previous_app_content = []
frontend_api = FrontEndAPI() 