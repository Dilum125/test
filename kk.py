name = input("Enter your name : ")
marks = int(input("Enter your marks : "))

if marks > 75:
    value = "A"
elif marks > 65:
    value = "B"
elif marks > 55:
    value = "C"
elif marks > 35:
    value = "S"
else:
    value = "F"

if marks >= 0 and marks <= 100:
    if marks > 75:
        value = "A"
    elif marks > 65:
        value = "B"
    elif marks > 55:
        value = "C"
    elif marks > 35:
        value = "S"
    else:
        value = "F"

print("Hello", name , "Your grade is", value)
