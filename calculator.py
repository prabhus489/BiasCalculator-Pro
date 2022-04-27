import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QGridLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.result_display = None
        self.result_str = ''
        self.create_ui()

    def create_ui(self):
        self.setWindowTitle('Calculator')
        vBoxLayout = QVBoxLayout()
        gridLayout = QGridLayout()

        button_txt_list = [["C", "^", "%", "/"],
                           ["7", "8", "9", "*"],
                           ["4", "5", "6", "-"],
                           ["1", "2", "3", "+"],
                           ["+/-", "0", ".", "="]]
        button_list = []
        for row in range(5):
            button_row_list = []
            for col, button_txt in enumerate(button_txt_list[row]):
                button = QPushButton(button_txt)
                button_row_list.append(button)
                gridLayout.addWidget(button, row, col)
                button.clicked.connect(self.button_clicked)
            button_list.append(button_row_list)

        self.result_display = QTextEdit()
        vBoxLayout.addWidget(self.result_display)
        vBoxLayout.addLayout(gridLayout)
        self.result_display.setFixedHeight(30)
        self.result_display.setFontPointSize(14)
        self.result_display.setText("0")
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        # self.result_display.setDisabled(True)

        self.setLayout(vBoxLayout)
        self.show()

    def button_clicked(self):
        # TODO: Implement Calculator logic
        sender = self.sender()
        button_txt = sender.text()
        if button_txt == "C":
            self.result_str = ""
        else:
            self.result_str += button_txt
        self.result_display.setText(self.result_str)
        self.result_display.setAlignment(Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())
