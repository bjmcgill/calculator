import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QSoundEffect

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(700, 300, 300, 400)
        
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: magenta; border: 2px solid black;")
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("background-color: cyan; color: black; border: 2px solid black; font-family: Helvetica; font-size: 36px; font-weight: bold; border-radius: 10px;")
        main_layout.addWidget(self.display)
        
        buttons_layout = QVBoxLayout()
        main_layout.addLayout(buttons_layout)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile(self.resource_path("click.wav")))
        
        for row in buttons:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.setFixedHeight(50)  # Set button height to 50
                button.setStyleSheet("background-color: yellow; color: black; border: 2px solid black; font-family: Helvetica; font-weight: bold; font-size: 36px; border-radius: 10px;")
                button.clicked.connect(self.on_button_clicked)
                row_layout.addWidget(button)
            buttons_layout.addLayout(row_layout)
        
        clear_button = QPushButton('Clear')
        clear_button.setFixedHeight(50)  # Set button height to 50
        clear_button.setStyleSheet("background-color: yellow; color: black; border: 2px solid black; font-family: Helvetica; font-weight: bold; font-size: 36px; border-radius: 10px;")
        clear_button.clicked.connect(self.clear_display)
        main_layout.addWidget(clear_button)

        self.current_expression = ""

    def on_button_clicked(self):
        button = self.sender()
        if button:
            print("Playing sound")
            self.sound_effect.play()
            text = button.text()
            if text == '=':
                try:
                    result = str(eval(self.current_expression))
                    self.display.setText(result)
                    self.current_expression = result
                except Exception as e:
                    self.display.setText("Error")
                    self.current_expression = ""
            elif text in {'+', '-', '*', '/', '.'}:
                self.current_expression += text
                self.display.setText(self.current_expression)
            else:
                self.current_expression += text
                self.display.setText(self.current_expression)

    def clear_display(self):
        print("Playing sound")
        self.sound_effect.play()
        self.current_expression = ""
        self.display.setText("")

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
