from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt

class settingsMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Settings")

        central_widget = QWidget(self)

        self.title = QLabel("Settings", self)
        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.title.resize(500, 100)

        container_widget = QWidget(central_widget)
        vLayout = QVBoxLayout(container_widget)
        vLayout.setSpacing(20)

        layout = QHBoxLayout()
        
        self.number_of_questions = QLabel("Number of questions:", self)
        self.number_of_questions.resize(200, 50)
        
        self.number_of_questions_input = QLineEdit(self)
        self.number_of_questions_input.resize(100, 25)
        self.number_of_questions_input.setText("5")
        self.number_of_questions_input.setInputMask("99")

        layout.addWidget(self.number_of_questions)
        layout.addWidget(self.number_of_questions_input)

        vLayout.addWidget(self.title)
        vLayout.addLayout(layout)

        layout2 = QHBoxLayout()
        label2 = QLabel("Difficulty:", self)
        
        input2 = QLineEdit(self)
        input2.setText("Hard")

        layout2.addWidget(label2)
        layout2.addWidget(input2)
        vLayout.addLayout(layout2)

        layout3 = QHBoxLayout()
        label3 = QLabel("Category:", self)

        input3 = QLineEdit(self)
        input3.setText("Anything!")

        layout3.addWidget(label3)
        layout3.addWidget(input3)
        vLayout.addLayout(layout3) 

        layout4 = QHBoxLayout()  
        label4 = QLabel("Model:", self)

        combo = QComboBox(self)
        combo.addItem("Fast")
        combo.addItem("Precise")

        layout4.addWidget(label4)
        layout4.addWidget(combo)

        vLayout.addLayout(layout4) 

        layout5 = QHBoxLayout()

        label5 = QLabel("Mode", self)

        combo2 = QComboBox(self)
        combo2.addItem("Flashcards")
        combo2.addItem("Quiz")

        layout5.addWidget(label5)
        layout5.addWidget(combo2)

        vLayout.addLayout(layout5)

        layout6 = QHBoxLayout()

        label6 = QLabel("Output", self)

        input4 = QLineEdit(self)
        input4.setText("")

        layout6.addWidget(label6)
        layout6.addWidget(input4)
        
        vLayout.addLayout(layout6)

        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(container_widget)
        self.setCentralWidget(central_widget)

class MainWindow(QMainWindow):
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


if __name__ == '__main__':
    # make corners round
    app = QApplication(sys.argv)
    main_window = MainWindow()
    settings = settingsMenu()
    
    # show settings menu
    settings.setGeometry(100, 100, 500, 500)
    settings.setFixedSize(500, 500)
    settings.show()
    
    
    sys.exit(app.exec_())
