word_list=["ABC", "abc"]

def all_title_case(word_list):
    #YOUR CODE HERE
    for word in word_list:
        is_title_case = word.istitle()
        if not is_title_case:
            return is_title_case


    return is_title_case


print(all_title_case(word_list)) #Should return False
