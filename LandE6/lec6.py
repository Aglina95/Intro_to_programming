import sys

#sort according to the name appears the most
freq = {}
dummy_list = ['Paloma','Martin','Martin','Paloma','Tofu', 'Martin']

#put list names in dictionairy
for name in dummy_list:
    #freq.setdefault(name, 0)

    #or

    if name in freq:
        freq[name] += 1
    else:
        freq[name] = 1

sorted_names = sorted(freq, key=freq.get, reverse=True) #from this dictionairy, get the values

#most_frequent_name = sorted_names[0]

#print(sorted_names)

'''#print the first element
print(sorted_names[0])'''

'''#print how many times 'Martin' appears
print(freq[sorted_names[0]])

#or
print(freq.get(sorted_names[0]))'''
