from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class HomeModule(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Life can be overwhelming, stay organised!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)