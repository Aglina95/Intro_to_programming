def all_title_case(word_list):

    for word in word_list:
        is_title_case = word.istitle()
        if not is_title_case:
            return is_title_case


    return is_title_case


'''dummy_list = [
"Hello",
"my Name is",
"James! James Bond"]'''

'''dummy_list = [
"Hello",
"My Name Is",
"James! James Bond"]'''

#print(all_title_case(dummy_list))
