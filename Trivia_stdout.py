import random

def TriviaFunction():
    print("Welcome!")
    question1 = input("Do you want to play? [y/n]")

    if question1.lower() != 'y':
        quit(1)
    else:
        print("Let's begin...")

    list = [
        {
            "question": "What is the capital of France?",
            "answer": "a",
            "possanswers": "a)Paris "
                           "b)Seville "
                           "c)Marseille "
        },
        {
            "question": "What is the capital of Spain?",
            "answer": "c",
            "possanswers": "a)Barcelona "
                           "b)Malaga "
                           "c)Madrid "
        },
        {
            "question": "What is the capital of Japan?",
            "answer": "a",
            "possanswers": "a)Tokyo "
                           "b)Osaka "
                           "c)Shanghai "
        },
        {
            "question": "What is the capital of Mexico?",
            "answer": "a",
            "possanswers": "a)Mexico City "
                           "b)Guadalajara "
                           "c)Kingston "
        },
        {
            "question": "What is the capital of Egypt?",
            "answer": "b",
            "possanswers": "a)Casablanca "
                           "b)Cairo "
                           "c)Lagos "
        },
        {
            "question": "What is the capital of Canada?",
            "answer": "c",
            "possanswers": "a)Toronto "
                           "b)Montreal "
                           "c)Ottawa "
        },
        {
            "question": "What is the capital of Australia?",
            "answer": "a",
            "possanswers": "a)Canberra "
                           "b)Sydney "
                           "c)Brisbane "
        }
    ]
    score = 0

    options = random.sample(range(len(list)), 3)

    print(options)

    for i in options:
        print(list[i]["question"])
        print(list[i]["possanswers"])
        input_answer = input("Your answer is: [a/b/c] ")
        if input_answer.lower() == list[i]["answer"]:
            score += 1

    print(f"Your final score is: {score}")


if __name__ == "__main__":
    TriviaFunction()