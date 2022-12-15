def shortest_word(word_list):
    shortest_word_list = sorted(word_list, key=len, reverse=False)

    if len(shortest_word_list) == 0:
        return None
    return shortest_word_list[0]


#dummy_list = ["ll", "b", "hhhh", "kkkkkk", "a"]
#dummy_list = []
#print(shortest_word(dummy_list))
