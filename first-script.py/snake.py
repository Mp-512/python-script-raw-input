names = input("input 4 names: ").split(",")
assignments = input("input 4 assignments: ").split(",")
grades = input("input 4 grades: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


for i in range(len(names)):
 
    print(message.format(names[i],assignments[i],grades[i],int(grades[i])+2*int(assignments[i])))