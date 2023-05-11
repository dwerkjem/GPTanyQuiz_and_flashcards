import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My PyQt5 App")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.text_edit_input = QTextEdit(self)
        self.text_edit_output = QTextEdit(self)

        self.text_edit_output.setReadOnly(True)

        process_button = QPushButton("Process Text", self)
        process_button.clicked.connect(self.process_text)

        layout.addWidget(self.text_edit_input)
        layout.addWidget(process_button)
        layout.addWidget(self.text_edit_output)

        self.setCentralWidget(central_widget)

    def process_text(self):
        input_text = self.text_edit_input.toPlainText()
        # Perform any processing on the input_text here
        output_text = input_text.upper()  # For example, convert the text to uppercase

        self.text_edit_output.setPlainText(output_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
