from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt
from quizAndFlash import quiz

class settingsMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def continueButton(self):
        mode = self.combo2.currentText()
        print(mode)
        self.close()
        self.quiz = quiz()
        if mode == "Quiz":
            self.quiz.show()
            
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

        self.combo2 = QComboBox(self)
        self.combo2.addItem("Flashcards")
        self.combo2.addItem("Quiz")

        layout5.addWidget(label5)
        layout5.addWidget(self.combo2)

        vLayout.addLayout(layout5)

        layout6 = QHBoxLayout()

        label6 = QLabel("Output", self)

        input4 = QLineEdit(self)
        input4.setText("")

        layout6.addWidget(label6)
        layout6.addWidget(input4)

        vLayout.addLayout(layout6)
        
        layout7 = QHBoxLayout()

        button = QPushButton("Continue", self)
        button.clicked.connect(self.continueButton)
        button.resize(100, 50)

        layout7.addWidget(button)

        vLayout.addLayout(layout7)
        

        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(container_widget)
        self.setCentralWidget(central_widget)
    
if __name__ == '__main__':
    # make corners round
    app = QApplication(sys.argv)
    settings = settingsMenu()
    
    # show settings menu
    settings.setGeometry(100, 100, 500, 500)
    settings.setFixedSize(500, 500)
    settings.show()
    
    sys.exit(app.exec_())
