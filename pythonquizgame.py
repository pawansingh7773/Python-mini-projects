#python quiz game
questions = ("What is India's national language?:",
              "Leap year occur in every? :",
             " who discovered gravity ?:",
             "who is prime minister of India?:")
options = (("A.English" , "B.Hindi" , "C.Marathi " , "D.Urdu "),
           ("A.5years" , "B.3years" , "C.4years " , "D.8years "),
           ("A.Newton" , "B.Enstien" , "C.Faraday " , "D.Ramanujan "),
           ("A.Rahulgandhi" , " B.NarendraModi" , "C.Donaldtrump " , "D.Viratkohli "))
answers = ("B", "C", "A", "B")
guesses = []
question_num = 0
score = 0
print("-------QUIZ STARTS------------")


for question in questions:
    print("------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("enter (A,B,C,D) :").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} : is correct answers")
    question_num += 1








print("-----------RESULT--------")
print(" answers :" , end=" ")
for answer in answers:
    print(answer , end=" ")
print()
print(" guesses :" , end=" ")
for guess in guesses:
    print(guess , end=" ")
print()
score = int(score/len(questions) * 100)
print(f"-----YOUR SCORE IS :{score}%")




