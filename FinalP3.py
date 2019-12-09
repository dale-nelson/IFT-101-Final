print("This program converts user-given characters to numbers dialed on a phone\n\
corresponding to that letter.\nMaximum of 10 characters allowed.")

char_list = ["0"] * 10
tmp_list = []

def userInput():
    return input("Please enter characters. ")

def maxCheck():
    given_string = userInput()
    while len(given_string) > 10:
        print("This is too many characters, please try again.")
        given_string = userInput()
    return given_string

def strToList():
    valid_string = maxCheck()
    for char in valid_string:
        tmp_list.append((char).lower())
    return tmp_list

def charToNum():
    tmp_list = strToList()
    for i in range(0,len(tmp_list)):
        if tmp_list[i] >= 'a' and tmp_list[i] <= 'c':
            tmp_list[i] = '2'
        if tmp_list[i] >= 'd' and tmp_list[i] <= 'f':
            tmp_list[i] = '3'
        if tmp_list[i] >= 'g' and tmp_list[i] <= 'i':
            tmp_list[i] = '4'
        if tmp_list[i] >= 'j' and tmp_list[i] <= 'l':
            tmp_list[i] = '5'
        if tmp_list[i] >= 'm' and tmp_list[i] <= 'o':
            tmp_list[i] = '6'
        if tmp_list[i] >= 'p' and tmp_list[i] <= 's':
            tmp_list[i] = '7'
        if tmp_list[i] >= 't' and tmp_list[i] <= 'v':
            tmp_list[i] = '8'
        if tmp_list[i] >= 'w' and tmp_list[i] <= 'z':
            tmp_list[i] = '9'
    return tmp_list

def addToList():
    tmp_list = charToNum()
    for i in range(0,len(tmp_list)):
        char_list[i] = tmp_list[i]
    return char_list

final_list = addToList()
print("The phone number is 1-" + ''.join(final_list[:3]) + "-"\
+ ''.join(final_list[3:6]) + "-" + ''.join(final_list[6:]))