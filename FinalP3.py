# Initialize the variables
sum_caps = 0  # Detecting number of capital letters
sum_lows = 0  # Detecting number of lower case letters
alpha_to_num = ''  # Translation of letters into numbers
phone_number = 'a'

while len(phone_number) != 0:

    # Prompt the user to imput variable
    print('Please enter a phone number or press <ENTER> to exit:')  #  Give user instructions
    phone_number = input()  # Define the variable #Note: may need to declare this a string later


    # Loop through the string to sum capital letters
    for counter in range(0, len(phone_number)):
        char = phone_number[counter]

        # Sum if capital
        if char.isupper():
            sum_caps += 1

    # Loop through the string to get sum of lower letters
    for counter in range(0, len(phone_number)):
        char = phone_number[counter]

        # Sum if lower
        if char.islower():
            sum_lows += 1


    # Loop through the string to convert letters to numbers
    for counter in range(0, len(phone_number)):
        char = phone_number[counter]

        
        if char >= 'A' and char <= 'C':
            alpha_to_num += '2'

        elif char >= 'a' and char <= 'c':
            alpha_to_num += '2'

        elif char >= 'D' and char <= 'F':
            alpha_to_num += '3'

        elif char >= 'd' and char <= 'f':
            alpha_to_num += '3'

        elif char >= 'G' and char <= 'I':
            alpha_to_num += '4'

        elif char >= 'g' and char <= 'i':
            alpha_to_num += '4'

        elif char >= 'J' and char <= 'L':
            alpha_to_num += '5'

        elif char >= 'j' and char <= 'l':
            alpha_to_num += '5'

        elif char >= 'M' and char <= 'O':
            alpha_to_num += '6'

        elif char >= 'm' and char <= 'o':
            alpha_to_num += '6'

        elif char >= 'P' and char <= 'S':
            alpha_to_num += '7'

        elif char >= 'p' and char <= 's':
            alpha_to_num += '7'

        elif char >= 'T' and char <= 'V':
            alpha_to_num += '8'

        elif char >= 't' and char <= 'v':
            alpha_to_num += '8'

        elif char >= 'W' and char <= 'Z':
            alpha_to_num += '9'

        elif char >= 'w' and char <= 'z':
            alpha_to_num += '9'

        else:
            alpha_to_num += char

    print(alpha_to_num)