# README.md

## anyQuize

anyQuize is a Python script that generates questions on a given topic using OpenAI's GPT-3.5-turbo or GPT-4 (if available) models. Users can choose between quiz mode or flashcard mode, specify the number of questions, and set the difficulty level.

### Prerequisites

- Python 3.x
- OpenAI Python library

### Installation

1. Install the OpenAI Python library:

   ```bash
   pip install openai
   ```

2. Set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

### Usage

```bash
python anyQuize.py <topic> [--mode MODE] [--number_of_questions N] [--difficulty DIFFICULTY] [--model MODEL] [--output OUTPUT]
```

#### Arguments

- `topic`: The topic of the questions (required)
- `--mode, -m`: The mode of the questions, quiz or flashcard (q/f) (default: "q")
- `--number_of_questions, -n`: The number of questions (default: 5)
- `--difficulty, -d`: The difficulty of the questions
- `--model, -M`: The model to use, fast or precise (f/p) (default: "f")
- `--output, -o`: The output file (default: "stdout")

### Example

```bash
python anyQuize.py "Python programming" --mode q --number_of_questions 10 --difficulty "intermediate" --model f --output "quiz_output.txt"
```

This command will generate 10 intermediate difficulty questions about Python programming in quiz mode, using the fast model (GPT-3.5-turbo), and save the output to a file called "quiz_output.txt".

### Notes

- In quiz mode, the script will ask the user for their answer to each question and then provide the correct answer along with an explanation.
- In flashcard mode, the script will generate questions and answers in the following format: '1: question1 \n A: answer1 \n 2: question2 \n A: answer2'
- The output file will be created or overwritten if it already exists.
