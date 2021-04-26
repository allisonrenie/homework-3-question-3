num = input("Please enter a year: ")
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
