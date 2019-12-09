def userInp():
    return input("Give me a number: ")

def loop():
    val = userInp()
    pos = 0
    while val != "0":
        if int(val) > 0:
            pos += 1
        val = userInp()
    return pos

print("You have entered {0} positive numbers.".format(loop()))