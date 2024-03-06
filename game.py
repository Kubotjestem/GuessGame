questions = (
    "What is the capital of France?",
    "What is the chemical symbol for water?",
    "Which planet is known as the Red Planet?",
    "What is the powerhouse of the cell?",
    "Who developed the theory of relativity?",
    "What is the largest mammal?",
    "What is the fastest land animal?",
    "How many continents are there in the world?"
)


options = [
    ("A. London", "B. Paris", "C. Berlin", "D. Rome"),
    ("A. H2O", "B. HO", "C. W2O", "D. H2"),
    ("A. Earth", "B. Jupiter", "C. Mars", "D. Venus"),
    ("A. Mitochondria", "B. Nucleus", "C. Ribosome", "D. Endoplasmic reticulum"),
    ("A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Stephen Hawking"),
    ("A. Elephant", "B. Blue whale", "C. Giraffe", "D. Hippopotamus"),
    ("A. Cheetah", "B. Lion", "C. Leopard", "D. Elephant"),
    ("A. Six", "B. Seven", "C. Eight", "D. Five")
]


answers = (
    "B",
    "A",
    "C",
    "A",
    "B",
    "B",
    "A",
    "B"
)

score = 0 
guesses = []
question_num = 0 


for question in questions: 
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("My awnser is (A, B, C, D): ").upper()
    guesses.append(guess)     

    if guess == answers[question_num]:
        print("-----Correct awnser!-----")
        score += 1
    else:
        print("-----Wrong awnser!-----")
        
    
    question_num += 1

score = score / len(questions) * 100 


print("-------------------------")
print(f"Correct awnsers: {answers}")
print(f"Your awnsers: {guesses}")
print(f"Your score is {score}%")


// dodaj commita do gita //

