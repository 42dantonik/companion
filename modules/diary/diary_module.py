from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPlainTextEdit, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

from visual.stylesheet import StyleSheet
from visual.format import Format
from visual.font import Font

class DiaryModule(QWidget):
    def __init__(self):
        super().__init__()
        self.styleTextBox = StyleSheet(bg_color="#dcaff2", radius="20px", format=Format(padding="20px 20px"))
        layout = QGridLayout(self)
        #layout.setRowMinimumHeight(1, 200)
        layout.setVerticalSpacing(20)
        label = QLabel("My Diary")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setStyleSheet(str(StyleSheet(font=Font(size="22px",color="#f3e7f9"))))

        textBox = QPlainTextEdit()
        textBox.setPlaceholderText("Your Diary Entry ...")
        textBox.setStyleSheet(str(self.styleTextBox))

        saveBtn = QPushButton("Save")
        saveBtn.setStyleSheet(str(StyleSheet(radius="10px", bg_color="#c9bed5" ,font=Font(size="22px"), format=Format(padding="5px 15px"))))
        layout.addWidget(label, 0, 1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(textBox, 1, 1)
        layout.addWidget(saveBtn, 2, 1, Qt.AlignmentFlag.AlignHCenter)