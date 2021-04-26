# Homework 1 Question 4
# Programmed by Allison Thompson
# Run my program by navigating to its location with the Command Prompt and
# typing in the full file name including .py. The program will then prompt you
# to type in a year. The program will prompt you until you enter a valid
# positive number. The program will then tell you if the year you entered
# is a leap year or not.

# get num from user
num = 0
isInt = False
while True:
    num = input("Please enter a year: ")
    # checking if the input can be converted to an int
    try:
        int(num)
    # if we get a ValueError, the num couldn't be converted, and is not an int
    except ValueError:
        continue
    # checking if the input is above 0
    if int(num) < 1:
        continue
    num = int(num)
    break

# is num divisible by 4?
divByFour = int(num % 4)
if divByFour == 0:
    # if yes, is num divisible by 100?
    divBy100 = int(num % 100)
    if divBy100 == 0:
        # if yes is num divisible by 400?
        divBy400 = int(num % 400)
        if divBy400 == 0:
            print(num, "is a leap year.")
        else:
            print(num, "is not a leap year.")
    else:
        print(num, "is a leap year.")
else:
    print(num, "is not a leap year.")
