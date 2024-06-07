# Built-ins
import sys
import os
import threading

# Utilities
import PyWebUI.utilities.util4code as u4c
import PyWebUI.utilities.util4string as u4s
import PyWebUI.utilities.util4files as u4f

# GUI
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Local imports
#import src.main as main
import PyWebUI.Functions as Functions
import PyWebUI.Globals as Globals
import PyWebUI.Frontend as Frontend
# Main Script must be imported last
import main_script

#________________________________________________________________________
#========================================================================

FRONTEND_SOCKET = Globals.FrontEndSocket(server=Frontend)
TITLE = Globals.app_config.project_name
MAIN_HTML = Globals.app_config.main_html
WIDTH, HEIGHT = Globals.app_config.window_size
#_______________________________________________________________________
#=======================================================================

class PyWebUIEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def contextMenuEvent(self, event):
        # Override the context menu event and do nothing to disable the right-click menu
        event.ignore()

    def dragEnterEvent(self, event):
        # Override the drag enter event and ignore it to disable dragging
        event.ignore()

    def dragMoveEvent(self, event):
        # Override the drag move event and ignore it to disable dragging
        event.ignore()

    def dragLeaveEvent(self, event):
        # Override the drag leave event and ignore it to disable dragging
        event.ignore()

    def dropEvent(self, event):
        # Override the drop event and ignore it to disable dragging
        event.ignore()

class AppWindow(QMainWindow): 
    def __init__(self):
        # GUI Initialization
        super().__init__()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, WIDTH, HEIGHT)
        self.setWindowTitle(TITLE)
        self.setEnabled(False)
        self.setWindowOpacity(0)
        # Initializing WebEngine
        self.browser = PyWebUIEngineView()
    
    #__OVERWRITTEN_FUNCTIONS____
    def onLoadFinished(self, success):
        if success:
            self.browser.page().toHtml(lambda *args,**kwargs: None)

    def keyPressEvent(self, event):
        """
        Checks all key press events made and their corresponding actions.
        """
        for event_key_object in Functions.KeyPressEvent.all_key_events:
            event_key_object.run(event)

    #__CUSTOM_FUNCTIONS_____
    def load_html(self) -> None:
        self.browser.load(QUrl.fromLocalFile(os.path.abspath(MAIN_HTML)))  # Load the HTML file
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  
        layout.addWidget(self.browser)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.browser.page().loadFinished.connect(self.onLoadFinished)

    def reveal_window(self, timer:QTimer) -> None:
        """
        Shows the window only if Frontend is connected. Stops timer if satisfied.
        """
        if Globals.Flags.Launcher.frontend_connected == True:
            self.setEnabled(True)  
            self.setWindowOpacity(1)
            timer.stop()
    
class App:
    def __init__(self):
        # Initializing pyQT application
        self.qt_app = QApplication(sys.argv)
        self.qt_window = AppWindow()
        Globals.App = self.qt_window
        self.qt_window.show()
    
    def catch_link(self) -> None:
        """
        Periodically checks if connection has been established into the frontend before revealing window.
        """
        self.connection_timer = QTimer()
        self.connection_timer.timeout.connect(lambda *args: self.qt_window.reveal_window(self.connection_timer))
        self.connection_timer.start(500)

    def run(self) -> None:
        FRONTEND_SOCKET.create() # Creates/runs front end socket
        self.qt_window.load_html()
        self.catch_link()
        sys.exit(self.qt_app.exec_())