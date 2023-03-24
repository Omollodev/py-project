quiz = {
    "question1": {
        "question": "What is yhe capital city of Kenya?",
        "answer": "Nairobi"
    },
    "question2": {
        "question": "What is the capital city of Uganda?",
        "answer": "Kampala"
    },
    "question3": {
        "question": "What is the capital city of Tanzania?",
        "answer": "Dodoma"
    },
    "question4": {
        "question": "What is the capital city of Somala? ",
        "answer": "Mogadishu"
    },
    "question5": {
        "question": "What is the capital city of Ethiopia?",
        "answer": "Addis Ababa"
    },
    "question6": {
        "question": "What is the capital city of Eritrea?",
        "answer": "Asmara"
    },
    "question7": {
        "question": "What is the capital city of South Sudan?",
        "answer": "Juba"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer: ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1
        print("Your score is:" + str(score))
        print("")
        print("")
    else:
        print("Wrong answer.")
        print("The answer is: " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")

print(f"You got {score} out of {len(quiz)}")
print(f"Your percentage is {score / 7 * 100} %")
