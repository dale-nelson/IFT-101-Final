def userInp():
    try:
        return (int(float(input("Give me an integer. "))))
    except ValueError:
        print("You didn't enter a number, please try again.")

def validateLoop():
    valid_check = userInp()
    while not valid_check:
        valid_check = userInp()
    return valid_check

def posCheck():
    a = ""
    while a != int(0):
        a = validateLoop()
        print("Thanks!")
    else:
        exit()
    return a

posCheck()