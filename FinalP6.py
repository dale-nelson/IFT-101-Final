main_string = "I know you know what I know"
str_to_list = main_string.split()
list_set = set(str_to_list)

for word in list_set:
    print("Frequency of {0} is {1}".format(word, str_to_list.count(word)))
