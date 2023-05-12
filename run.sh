#!/bin/bash
# This script is used to run the program

if [ $# -eq 0 ]; then
    python3 ~/DEVELOPER/GPTanyQuiz_and_flashcards/menuQT.py
else
    python3 ~/DEVELOPER/GPTanyQuiz_and_flashcards/anyQuizeCLI.py
fi