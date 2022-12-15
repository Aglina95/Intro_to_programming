# Write your code here :-) split the string into a list and check len
string = 'The children are disappearing!'

words = []

for word in string.split():
    if len(word) == 0:
        continue
    else:
        words.append(word)

#print(words)

#print(len(words))


