def userInp():
    try:
        return float(input(""))
    except ValueError:
        print("Your entry was not a number. Please try again.")

def validLoop():
    val_check = userInp()
    while not val_check:
        val_check = userInp()
    return val_check

def posCheck():
    pos_check = validLoop()
    while pos_check < 0:
        print("Your entry must be positive. Negative values cannot be accepted.")
        pos_check = validLoop()
    return pos_check

def oneTwoOrThree():
    in_range = posCheck()
    while in_range < 0 or in_range > 3:
        print("Please enter 1, 2, or 3.")
        in_range = posCheck()
    return in_range

def convert(a,b):
    if b == 1:
        ouncesToLbs(a)
    if b == 2:
        ouncesToLiters(a)
    if b == 3:
        ouncesToGallon(a)

def ouncesToLbs(a):
    converted = (a/16)
    print("{0} ounces is {1}lbs.".format(a, round(converted, 2)))

def ouncesToLiters(a):
    converted = (a/33.814)
    print("{0} ounces is {1} liters.".format(a, round(converted, 2)))

def ouncesToGallon(a):
    converted = (a/128)
    print("{0} ounces is {1} gallons.".format(a, round(converted, 2)))

print("This program takes 2 inputs from the user. The first input is ounces.\n\
The second input, you decide how you want the ounces converted.\n\
Enter 1 for pounds\n\
Enter 2 for liters\n\
Enter 3 for gallons")

print("First, please enter the number of ounces.")
is_pos = posCheck()
print("Now, please enter 1, 2, or 3.")
in_range = oneTwoOrThree()
convert(is_pos, in_range)