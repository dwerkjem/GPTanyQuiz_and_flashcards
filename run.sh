#!/bin/bash
# This script is used to run the program
if [ $# -eq 0 ]; then

    python3 "$(pwd)"/python/menuQT.py
else
    python3 "$(pwd)"/python/anyQuizeCLI.py
fi