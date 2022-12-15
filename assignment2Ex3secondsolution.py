# take the first smallest string from list
def shortest_word(word_list):
    #return None if list is empty
    if len(word_list) == 0:
        return None

    #min_word_length = len(word_list[0]) = word in list with minimum length
    min_word_length = len(word_list[0])
    #word/element in list
    word_in_list_str = word_list[0]

    for word in word_list:
        #if the lenght of the word is less than the word in the length of the current minimum length word
        if len(word) < min_word_length:
           word_in_list_str = word
           min_word_length = len(word)

    return word_in_list_str


#dummy_list = ["ssssssss", "leg", "zsss", "ssssewere", "egg"]
#dummy_list = []
#print(shortest_word(dummy_list))

# take the last smallest string from list
def shortest_last_word(word_list):

    if word_list and len(word_list) == 0:
        return None

    min_word_length = len(word_list[0])
    word_in_list_str = word_list[0]

    for word in word_list:
        if len(word) <= min_word_length:
           word_in_list_str = word
           min_word_length = len(word)

    return word_in_list_str

#how to search a specific element in list
def word_exists(word_list, word_in_list_str):

    if len(word_list) == 0:
        return False

    for word in word_list:
        if word == word_in_list_str:
           return True

    return False

