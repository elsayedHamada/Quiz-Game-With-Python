# Welcome Message
print("Welcome To Quizey Game With Mr Jack😉.")
start = input("Do you Want To Play Or Not (y/n) >>").lower()
# Score
score = 0
# Close The Game
if start != "y":
    print("See You Later😎.")
    quit()
# Welcome Message
print("Note>> if you answer right you get 1 score and if wrong you lose one")
print("Note>> This Game is 7 questions")
print("Let's Start With the First Question.")


# Check Answer
def answer_checker(q, a, s):
    if q == a:
        print("You Got it.")
        s += 1
        print(f"Your Score is {s}")
    else:
        if s == 0:
            print("sorry, Wrong")
            s = 0
            print(f"Your Score is {s}")
        else:
            print("sorry, Wrong")
            s -= 1
            print(f"Your Score is {s}")
    print(f"Answer >> {a}")


# Q and A
while True:
    Q1 = input("Who Is The First Man On The Moon? ").lower()
    A1 = "neil armstrong"
    answer_checker(Q1, A1, score)

    Q2 = input("and Which Flight He Was On? ").lower()
    A2 = "apollo 11"
    answer_checker(Q2, A2, score)

    Q3 = input("Which is the smallest planet within our solar system? ").lower()
    A3 = "mercury"
    answer_checker(Q3, A3, score)

    Q4 = input("Which is the second smallest planet within our solar system? ").lower()
    A4 = "mars"
    answer_checker(Q4, A4, score)

    Q5 = input("Which is the brightest planet in the night’s sky? ").lower()
    A5 = "venus"
    answer_checker(Q5, A5, score)

    Q6 = input("Which planet is larger, Neptune or Saturn? ").lower()
    A6 = "saturn"
    answer_checker(Q6, A6, score)

    Q7 = input("There have been more missions to this planet versus any other planet? ").lower()
    A7 = "mars"
    answer_checker(Q7, A7, score)

    print("-----------------------")
    print(f"Your Score >> {score}")
    print("-----------------------")

    if 5 < score:
        print("You Did A Great Job Here🐱‍")
    elif 3 < score < 5:
        print("You Did Good Job 😊")
    else:
        print("You Will Better in the next Time.")

    again = input("Do Want To Play again (y/n)>>").lower()
    if again == "y":
        continue
    else:
        break
# The End.
