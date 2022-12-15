# Write your code here :-)
def has_friend(friends, friend):
    for f in friends:
        if f == friend:
            return True

    return False

def people_they_know(friends_anna, friends_betty):
    common = []
    for friend_anna in friends_anna:
        if not has_friend(common, friend_anna):
            common.append(friend_anna)
        for friend_betty in friends_betty:
            if not has_friend(common, friend_betty):
                common.append(friend_betty)

    return len(common)

#find where it crashes: usually try the ones in the middle
list_1 = list(range(500))
list_2 = list(range(500))

print(people_they_know(list_1, list_2))

#for loops with same indentation don't add complexity: For instance
#in here in the people_they_know() function
        """if not has_friend(common, friend_anna):
            common.append(friend_anna)
        for friend_betty in friends_betty:"""

#has_friend has a for loop and also the same indentationwith the for loop. so they are not considered nested and therefore
#there's no additional complexity
