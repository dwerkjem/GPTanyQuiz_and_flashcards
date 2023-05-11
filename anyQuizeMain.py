import openai
import os


# OpenAI API key

openai.api_key = os.environ.get("OPENAI_API_KEY")

topic = input("Enter a topic: ")
mode = input("Enter the mode, quiz or flashcard (q/f): ")
if mode != "q" and mode != "f":
    print("Invalid input, using default mode")
    mode = "q"
number_of_questions = input("Enter the number of questions: ")
difficulty = input("Enter the difficulty: ")
model = input("Enter the model fast or precise (f/p): ")

if model == "f":
    model = "gpt-3.5-turbo"
elif model == "p":
    model = "gpt-4"
else:
    print("Invalid input, using default model")
    model = "gpt-3.5-turbo"
if mode == "f":
    message = openai.ChatCompletion.create(
        model=model,
    messages=[
            {"role": "system", "content": f"you make {number_of_questions} {difficulty} questions on the topic {topic} in this format: '1: question1 \n A: answer1 \n 2: question2 \n A: answer2 '"},
        ]
    )

    print('please wait for the model to respond...')

    print(message["choices"][0]["message"]["content"])
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
        print(new["choices"][0]["message"]["content"])
        correct = input("did you answer correctly? (y/n): ")
        if correct == "y":
            score += 1
            total += 1
        elif correct == "n":
            total += 1
        else:
            print("invalid input, not counting as correct or incorrect")
    print("results".center(50, "-"))
    print(f"you got {score} out of {total} correct or {score/total*100}%")
