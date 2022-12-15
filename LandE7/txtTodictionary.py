# txt file list to dictionary

dictionary = {}
with open("sales.txt") as file:
 for line in file:

    (key, value) = line.split()

    dictionary[int(key)] = value

print ('\ntext file to dictionary=\n',dictionary)
