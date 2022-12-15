def read_file(filename):

    dictionary = {}
    with open(filename) as file_object:
        for line in file_object:
            k, v = line.strip().split(';')
            if int(v) >= 8:
                dictionary[k.strip()] = v.strip()

    return dictionary

def merge_dicts(dict1, dict2):
    matching_keys = []
    for key in dict1.keys():
        if key in dict2:
            matching_keys.append(key)

    return matching_keys

def print_movies(list_of_movies):
    for movie in list_of_movies:
        print(movie)

def print_common_movies(filename1, filename2):
    movies1 = read_file(filename1)
    movies2 = read_file(filename2)
    common_movies = merge_dicts(movies1, movies2)

    print_movies(common_movies)

print_common_movies("leah.txt", "marie.txt")

