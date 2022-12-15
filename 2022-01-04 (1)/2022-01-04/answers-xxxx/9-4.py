def people_they_know(friends_anna, friends_betty):
    # TODO: Implement me!
    # Your code comes here:
    #Linear complexity
    #friends_dictionary = {**friends_anna, **friends_betty} dictionary solution
    friends_set = friends_anna.union(friends_betty)
    #friends_set = friends_anna.intersection(friends_betty) intersection = common
    print(len(friends_set))


friends_anna = {"Cecilie", "Katrine", "Rasmus"}
"""#add items into dictionary
friends_anna["Cecilie"] = "annafirend1"
friends_anna["Katrine"] = "annafriend2"
friends_anna["Rasmus"] = "annafriend3"""

friends_betty = {"Rasmus", "Adam"}

"""friends_betty["Rasmus"] = "bettyfriend1"
friends_betty["Adam"] = "bettyfriend2"""

#print(friends_anna)
#print(friends_betty)
people_they_know(friends_anna, friends_betty)
