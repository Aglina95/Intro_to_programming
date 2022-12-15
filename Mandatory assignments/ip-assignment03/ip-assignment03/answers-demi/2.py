interests = {
    'Sophia' : 'Computer',
    'Anders' : 'Dancing',
    'Mette' : 'Dancing',
    'Hikari' : 'Computer',
    'Riko' : 'Rowing',
    'Troels' : 'Rowing',
    'Sarah' : 'Rowing'
}

def transform_dictionary(dictionary):
    #YOUR CODE HERE
    new_dict = {}

    for key, value in dictionary.items():
        if not value in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value] += [key]


    return new_dict


print(transform_dictionary(interests)) # [except order of elements] it should print  {'Computer': ['Sophia', 'Hikari'], 'Dancing': ['Anders', 'Mette'], 'Rowing': ['Riko', 'Troels', 'Sarah']}
