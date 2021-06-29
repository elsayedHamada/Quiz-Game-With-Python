print("Welcome To Quizey Game With Mr Jack😉.")
start = input("Do you Want To Play Or Not (y/n) >>").lower()
score = 0
if start != "y":
    print("See You Later😎.")
    quit()
# Welcome Message
print("Note>> if you answer right you get 1 score and if wrong you lose one")
print("Note>> This Game is 7 questions")
print("Let's Start With the First Question.")


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

