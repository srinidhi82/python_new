marks = int(input('Enter your score: '))

if marks > 90:
    print("Congratulations! You have scored A+")
elif marks >= 80 and marks <= 90:
    print("Congratulations! You have scored A-")
else:
    print("Sorry. You have not passed this course")