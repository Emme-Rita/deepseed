import time

quiz = {
    "history": {
        "easy": [
            {
                "question" : "who disccovered river wouri",
                "answer": ["A. Mr Zingraff", "B. ", "C. ", "D. "],
                "correc_ans" : "A. Mr Zingraff"
            }
        ],
        "hard": [
            {
                "question" : "who disccovered river wouri",
                "answer": ["A. Mr Zingraff", "B. ", "C. ", "D. "],
                "correc_ans" : "A. Mr Zingraff"
            }
        ]
    },  
    "chemistry": {
        "easy": [
            {
                "question" : "who disccovered river wouri",
                "answer": ["A. Mr Zingraff", "B. ", "C. ", "D. "],
                "correc_ans" : "A. Mr Zingraff"
            }
        ],
        "hard": [
            {
                "question" : "who disccovered river wouri",
                "answer": ["A. Mr Zingraff", "B. ", "C. ", "D. "],
                "correc_ans" : "A. Mr Zingraff"
            }
        ]
    },
    "maths": {
        "easy": [
            {
                "question" : "who disccovered river wouri",
                "answer": ["A. Mr Zingraff", "B. ", "C. ", "D. "],
                "correc_ans" : "A. Mr Zingraff"
            }
        ],
        "hard": [
            {
                "question" : "who disccovered river wouri",
                "answer": ["A. Mr Zingraff", "B. ", "C. ", "D. "],
                "correc_ans" : "A. Mr Zingraff"
            }
        ]
    }    
}
score = 0
categories = list(quiz.keys())
choose = input(f"enter a category from the categories {categories}: ")
if choose in categories:
    difficulty = list(quiz[choose].keys()) 
    level = input(f"Choose a difficulty level {difficulty}: ")
    if level in difficulty:
        print(f"selected: {choose} ({level})")
        questions = quiz[choose][level]
        for i, j in enumerate(questions, start = 1):
            start_time = time.time()
            print(f"\n Q{i}.  {j["question"]} ")
            for k, option in enumerate(j["answer"]):
                print(f"{k}. {option}")
            answer = int(input("your answer from (0-3)"))
            if answer == j["correc_ans"]:
                print("Correct")
                score += 20
            else:
                print(f"wrong answer. the correct answer: {j["correc_ans"]}") 
            end_time = time.time()
            tim = round(end_time - start_time)
            progress = int((i/len(questions)*100))
            bar = "#"*(progress//10) + "-" * (10-(progress//10))
            print(f"progress bar: [{bar}] {progress}% completed")
            print(f"time taken for question: {tim} seconds")
    else:
         print("choose from the specified difficulty")
else:
    print("choose from the specified category")

print("quiz finished")
print(f"Score: {score}/{len(questions)*20}")
