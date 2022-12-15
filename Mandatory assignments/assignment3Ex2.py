import pprint

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
    new_dict = {}

    for key, value in dictionary.items():
        if not value in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value] += [key]


    return new_dict

#run with pprint
#pprint.pprint(transform_dictionary(interests))











