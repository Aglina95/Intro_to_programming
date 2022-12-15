# Write your code here :-)
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    previous_value = count[character]
    count[character] = previous_value + 1 #dictionairy[key] = value


#set default
#if character in count:
    #pass
#else:
    #count[character] = 0
