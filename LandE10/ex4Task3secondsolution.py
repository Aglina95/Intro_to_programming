# Write your code here :-)
def read_file(filename):

    dictionary = {}
    with open(filename) as file_object:
        for line in file_object:
            k, v = line.strip().split(';')
            if int(v) >= 8:
                dictionary[k.strip()] = v.strip()

    return dictionary

def merge_dicts(dict1, dict2):
   new_dict = {**dict1, **dict2}

   return new_dict

"""print("Leah:")
print(read_file("leah.txt"))
print()
print("Marie:")
print(read_file("marie.txt"))
print()"""
print(merge_dicts(read_file("marie.txt"), read_file("leah.txt")))
