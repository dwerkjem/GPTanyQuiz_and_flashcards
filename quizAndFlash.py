from PyQt5.QtWidgets import *
from gptRes import ChatAssistant as chat
class quiz(QMainWindow):
    def __init__(self, model, mode, numQuestions, topic, difficulty, out):
        super().__init__()
        self.model = model
        self.mode = mode
        self.numQuestions = numQuestions
        self.topic = topic
        self.difficulty = difficulty
        self.out = out
        self.init_ui()
        
        
    
    def init_ui(self):
        self.setWindowTitle(f"quiz on {self.topic}")
        self.setGeometry(100, 100, 500, 500)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        
        
        self.question = QLabel(self)
        self.text_edit_input = QTextEdit(self)
        self.text_output = QLabel(self)

        process_button = QPushButton("Process Text", self)
        process_button.clicked.connect(self.process_text)

        layout.addWidget(self.question)
        layout.addWidget(self.text_edit_input)
        layout.addWidget(process_button)
        layout.addWidget(self.text_output)
        self.setCentralWidget(central_widget)

    def process_text(self):
        input_text = self.text_edit_input.toPlainText()
        # Perform any processing on the input_text here
        
