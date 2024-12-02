from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent

from data.themes import Themes
from modules.home_module import HomeModule
from modules.talea_module import TaleaModule

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Companion")
        self.resize(1000, 600)

        # Initialize UI
        self.load_ui()

        # # Add Modules
        self.add_modules()

    def load_ui(self):
        """Set up the main UI layout and components."""
        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main Layout
        self.main_layout = QHBoxLayout(self.central_widget)

        # Navigation Menu
        self.create_nav_menu()
        self.main_layout.addWidget(self.nav_menu)

        # Stacked Widget for Modules
        self.stack = QStackedWidget()
        self.main_layout.addWidget(self.stack)

    def create_nav_menu(self):
        """Create the navigation menu with buttons."""
        self.nav_menu = QWidget()
        self.nav_menu_layout = QVBoxLayout(self.nav_menu)
        self.nav_menu_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.nav_menu.setStyleSheet(Themes.NAV_MENU)

        # Dynamically create navigation buttons
        for index, (label,_) in enumerate(self.modules_config()):
            button = QPushButton(label)
            button.clicked.connect(lambda _, idx=index: self.switch_module(idx))
            self.nav_menu_layout.addWidget(button)

    def modules_config(self):
        """Define the list of modules and their labels."""
        return [
            ("Home", HomeModule),
            ("Talea", TaleaModule),
        ]

    def add_modules(self):
        """Dynamically add modules to the stack."""
        #self.modules = {} #what for?
        for label, module_class in self.modules_config():
            #module_instance = (
            #    module_class() if hasattr(module_class, "__init__") else module_class() # why??
            #)
            module_instance = module_class()
            self.stack.addWidget(module_instance)
            #self.modules[label] = module_instance

    def switch_module(self, index):
        """Switch module in the stacked widget."""
        self.stack.setCurrentIndex(index)

    def keyPressEvent(self, event: QKeyEvent):
        """Close the application when the Escape key is pressed."""
        if event.key() == Qt.Key.Key_Escape:
            self.close()