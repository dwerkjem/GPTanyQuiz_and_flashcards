import openai
import os
import logging
import argparse

# Argument parser

parser = argparse.ArgumentParser(description="anyQuize")
parser.add_argument("topic", type=str, help="the topic of the questions")
parser.add_argument("--mode", "-m",default="q", type=str,choices=("q","f"), help="the mode of the questions, quiz or flashcard (q/f)")
parser.add_argument("--number_of_questions","-n",default=5, type=int, help="the number of questions")
parser.add_argument("--difficulty","-d", type=str, help="the difficulty of the questions")
parser.add_argument("--model","-M",default="f",choices=("f","p"), type=str, help="the model to use, fast or precise (f/p)")
parser.add_argument("--output","-o",default="stdout", type=str, help="the output file") 
args = parser.parse_args()


# Logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# OpenAI API key

openai.api_key = os.environ.get("OPENAI_API_KEY")

topic = args.topic
mode = args.mode
number_of_questions = args.number_of_questions
difficulty = args.difficulty
model = args.model
output = args.output

if model == "f":
    model = "gpt-3.5-turbo"
elif model == "p":
    model = "gpt-4"
if mode == "f":
    print("setting up flashcards...")
    message = openai.ChatCompletion.create(
        model=model,
    messages=[
            {"role": "system", "content": f"you make {number_of_questions} {difficulty} questions on the topic {topic} in this format: '1: question1 \n A: answer1 \n 2: question2 \n A: answer2 '"},
        ]
    )
    print("flashcards".center(50, "-"))

    if output == "stdout":
        print(message["choices"][0]["message"]["content"])
    else:
        with open(output, "w") as f:
            f.write(message["choices"][0]["message"]["content"])
elif mode == "q":
    score = 0
    total = 0
    print('please wait for the model to make the questions...')
    message = openai.ChatCompletion.create(
        model=model,
    messages=[
            {"role": "system", "content": f"you make {number_of_questions} {difficulty} questions on the topic {topic} in this format: 'question1 \n question2 \n question3'"},
        ]
    )
    questions = message["choices"][0]["message"]["content"].split("\n")
    for i in range(len(questions)):
        if questions[i] != "":
            pass
        else:
            questions[i] = questions[i].strip()
    for question in questions:
        if question == "":
            continue
        print("question".center(50, "-"))
        print(question)
        user = input("Enter the answer: ")
        new = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": f"is the answer to the question {question}. {user} if it is correct please respond with correct and nothing else, if it is not correct write incorrect and the correct answer and why it is correct"}
        ]
        )
        print("answer".center(50, "-"))
        res = (new["choices"][0]["message"]["content"])
        print(res)
        correct = input("did you answer correctly? (y/n): ")
        if correct == "y":
            score += 1
            total += 1
        elif correct == "n":
            total += 1
        
        print("invalid input, not counting as correct or incorrect")
        with open(output, "a") as f:
            f.write(f"question number {total}".center(50, "-")+ "\n")
            f.write(f"question:\t{question}\n")
            f.write(f"user:\t{user}\n")
            f.write(f"answer:\t{res}\n")
            f.write(f"correct:\t{correct}\n")
            f.write("\n")

    print("results".center(50, "-"))
    print(f"you got {score} out of {total} correct or {score/total*100}%")
    
