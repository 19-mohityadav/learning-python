# Python Quiz Game

questions = ("How many elements are there in the periodic table?: ",
             "Which is largest cell in the Earth?: ",
             "Which is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")


options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Plant", "B. Animal", "C. Amoeba", "D. Egg"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 300", "B. 298", "C. 206", "D. 106"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print()
print()
print("----------------------------------------------------------------------------------------")
print("                                             RESULTS                                    ")
print("----------------------------------------------------------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your final score is {score}%")

