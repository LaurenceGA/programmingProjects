print("Quiz time!\n")

correct = 0


class question:
    def __init__(self, typ, question, options, answer):
        self.typ = typ
        self.question = question
        self.options = options
        self.answer = answer

questions = [
    question(
        "bool",
        "2+2 = 5",
        "True or False\n>>>",
        True
    ),
    question(
        "number",
        "What is the fifth digit of pi?",
        ">>>",
        5
    ),
    question(
        "multi",
        "What did the quick blue fox jump over?",
        "A: The lazy dog\nB: the not so lazy cow\nC: Foxes can't jump\nD: The green dog\n>>>",
        4
    ),
    question(
        "string",
        "Who wrote Dracula?",
        ">>>",
        "bram stoker"
    ),
    question(
        "number",
        "What is the meaning of life?",
        ">>>",
        42
    )
]

def strtobool(str):
    if str.lower() in ['t', 'true']:
        return True
    elif str.lower() in ['f', 'false']:
        return False
    else:
        return False

def strtomulti(str):
    try:
        return int(str)
    except ValueError:
        if len(str) > 1:
            return -1
        else:
            return ord(str.lower()) - 96

def askbool(q, answer):
    ansBool = strtobool(answer)
    if ansBool == q.answer:
        print("Correct!")
        return 1
    else:
        print("Nope.")
        return 0

def asknum(q, answer):
    try:
        num = float(answer)

        if num == q.answer:
            print("Correct!")
            return 1
        else:
            print("Nope.")
            return 0

    except ValueError:
        print("Unacceptable answer.\nIncorrect!")
        return 0

def askmulti(q, answer):
    ansMul = strtomulti(answer)
    if ansMul == q.answer:
        print("Correct!")
        return 1
    else:
        print("Nope.")
        return 0

def askstring(q, answer):
    if answer.lower() == q.answer:
        print("Correct!")
        return 1
    else:
        print("Nope.")
        return 0

for question in questions:
    print(question.question)
    inp = input(question.options)
    if question.typ == "bool":
        correct += askbool(question, inp)
    elif question.typ == "number":
        correct += asknum(question, inp)
    elif question.typ == "multi":
        correct += askmulti(question, inp)
    elif question.typ == "string":
        correct += askstring(question, inp)
    else:
        correct += 1

    print()

print("You got %d/%d. That's %.1f%% correct!" % (correct, len(questions), correct/len(questions)*100))
if correct <= 1:
    print("You're bad at this.")