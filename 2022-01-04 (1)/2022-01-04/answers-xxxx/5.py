favorite_places = {} # Do not change this line.

#add items into dictionary
favorite_places["Sarah"] = "Spain"
favorite_places["Peter"] = "Italy"
favorite_places["Thore"] = "Spain"

#print(favorite_places)

def print_fav_places(dict):
    for person, place in dict.items():
        print(person, "'s favorite place is", place)

print_fav_places(favorite_places)

#count how many times a value appears
def count_favorites(favorite_places, place):

    count = 0
    for v in favorite_places.values():
        if v == place:
            count += 1

    return count


print(count_favorites(favorite_places, "Spain"))



