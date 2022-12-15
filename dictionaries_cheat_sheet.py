# Write your code here :-)
#Cheatsheet for Dictionaries
d = {} # creates an empty dictionary
d['name'] = 'Sophia' # new entry ('name', 'Sophia') in the dictionary
d['age'] = 30 # new entry ('age', 30) in the dictionary
print(d['age']) # access the value of the key 'age' in the dictionary (here, 30)
print(d['city']) # doesn't work, because there is no key 'city' in the dictionary

for k in d: # iterates through all the keys
  print(k, d[k])  # print the keys and the associated values

for k in sorted(d): # iterates through all the keys in sorted order
  print(k, d[k])

for k in sorted(d, key=d.get): # iterates through all the keys, sorted by their values
  print(k, d[k])
