#!/bin/bash
# This script is used to run the program

if [ $# -eq 0 ]; then
    python3 anyQuizeQT.py
else
    python3 anyQuizeCLI.py "$@"
fi