mathStudents = ['Audrey', 'Ben', 'Julia', 'Paul', 'Gerry', 'Sue', 'Helena', 'Harry', 'Marco', 'Rachel', 'Tina', 'Mark', 'Jackson']
csStudents = ['William', 'Aroha', 'Melissa', 'Sue', 'Ben', 'Audrey', 'Susan', 'Mark', 'Hemi', 'Brendan', 'Paul', 'Barry', 'Julia']

totalStudents = 0

for mathS in mathStudents:
    for comS in csStudents:
        if mathS == comS:
            print("Studnet:\t%s is enrolled in both classes" % mathS)
            totalStudents += 1
print(totalStudents, "students are enrolled in both classes")