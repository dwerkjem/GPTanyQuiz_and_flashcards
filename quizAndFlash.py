from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("My PyQt5 App")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        
        self.question = QLabel(self)
        self.text_edit_input = QTextEdit(self)
        self.text_edit_output = QLabel(self)

        process_button = QPushButton("Process Text", self)
        process_button.clicked.connect(self.process_text)

        layout.addWidget(self.question)
        layout.addWidget(self.text_edit_input)
        layout.addWidget(process_button)
        layout.addWidget(self.text_edit_output)
        self.setCentralWidget(central_widget)


    def process_text(self):
        input_text = self.text_edit_input.toPlainText()
        # Perform any processing on the input_text here
        output_text = input_text.upper()  # For example, convert the text to uppercase
        self.text_edit_output.setText(output_text)
