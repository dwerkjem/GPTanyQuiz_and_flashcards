# OpenAI Quiz and Flashcard Generator

This script generates quizzes and flashcards based on a given topic using OpenAI's GPT-3.5-turbo or GPT-4 models. Users can specify the number of questions, difficulty, and the model to use.

## Requirements

- Python 3.x
- OpenAI Python library
- A paid account with open AI

## Installation

1. Install the OpenAI Python library:

```bash
pip install openai
```

2. Set your OpenAI API key as an environment variable:

If you don't have one you can get one [here](https://platform.openai.com/account/billing/overview)

```bash
export OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script with:

```bash
python quiz_flashcard_generator.py
```

You will be prompted to enter the following information:

- Topic: The subject for the quiz or flashcards
- Mode: Choose between quiz (q) or flashcard (f) mode
- Number of questions: The desired number of questions or flashcards
- Difficulty: The level of difficulty for the questions
- Model: Choose between fast (f) or precise (p) model

In quiz mode, the script will generate questions and ask for your answers. After each question, the script will check if your answer is correct and provide the correct answer if necessary. At the end of the quiz, it will display your score and percentage of correct answers.

In flashcard mode, the script will generate questions with their respective answers in the following format:

```text
1: question1
A: answer1
2: question2
A: answer2
```

## Example

```input
Enter a topic: Python programming
Enter the mode, quiz or flashcard (q/f): q
Enter the number of questions: 5
Enter the difficulty: easy
Enter the model fast or precise (f/p): f
```

This will generate a 5-question quiz on Python programming with easy difficulty using the fast GPT-3.5-turbo model.
