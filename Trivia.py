question1 = input("Do you want to play? [y/n]")

if question1.lower() != 'n'and question1.lower() != 'y':
    raise Exception("You didn't enter a valid value.")

if question1.lower() == 'y':
    print("Let's begin...")

    question_indices = {
        "1": "What is the capital of France?",
        "2": "What is the capital of Spain?",
        "3": "What is the capital of Japan?",
        "4": "What is the capital of Mexico?",
        "5": "What is the capital of Egypt?"
    }

    rightanswer_indices = {
        "1": "a",
        "2": "c",
        "3": "a",
        "4": "a",
        "5": "b"
    }

    possibleanswers_indices = {
        "1": "a)Paris "
             "b)Seville "
             "c)Marseille ",
        "2": "a)Barcelona "
             "b)Malaga "
             "c)Madrid ",
        "3": "a)Tokyo "
             "b)Osaka "
             "c)Shanghai ",
        "4": "a)Mexico City "
             "b)Guadalajara "
             "c)Kingston ",
        "5": "a)Casablanca "
             "b)Cairo "
             "c)Lagos "
    }

    score = 0

    for i in range(1,4):
        print(question_indices.get(str(i)))
        print(possibleanswers_indices.get(str(i)))
        input_answer = input("Your answer is: [a/b/c] ")
        if input_answer == rightanswer_indices.get(str(i)):
            score += 1

    print(f"Your final score is: {score}")