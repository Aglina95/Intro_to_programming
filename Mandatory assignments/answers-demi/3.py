def shortest_word(word_list):

    if len(word_list) == 0:
        return None

    min_word_length = len(word_list[0])
    word_in_list_str = word_list[0]

    for word in word_list:
        if len(word) < min_word_length:
           word_in_list_str = word
           min_word_length = len(word)

    return word_in_list_str


#dummy_list = ["ssssssss", "leg", "zsss", "ssssewere", "egg"]
#dummy_list = []
#print(shortest_word(dummy_list))
