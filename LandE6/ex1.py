people = []

leo_dictionairy = {"first_name": "Leo",
                    "last_name": "Davies",
                    "age": "19",
                    "city": "Copenhagen"}



amy_dictionaity = {"first_name": "Amy",
                    "last_name": "Winehouse",
                    "age": "28",
                    "city": "L.A"
                    }
nameless_king_dictionaity = {"first_name": "Nameless",
                    "last_name": "King",
                    "age": "3000",
                    "city": "Archdragon Peak"
                    }

leo_list = list(leo_dictionairy.items())
#print(leo_list)
amy_list = list(amy_dictionaity.items())
#print(amy_list)
nameless_king_list = list(nameless_king_dictionaity.items())
#print(nameless_king_list)


people = leo_list + amy_list + nameless_king_list



for person in people:

    print(person)

