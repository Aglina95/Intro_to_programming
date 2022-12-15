# Write your code here :-)
'''
#storing the lines in a list and then working with them outside the with block.

list_var = []

filename = 'pi_learned.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

for line in range(3):
    list_var.append(pi_string)
print(list_var)

'''

'''
#print line from txt file 3 times

filename = 'pi_learned.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

for line in range(3):
    print(pi_string)'''


''' read lines
filename = 'pi_learned.txt'
with open(filename) as file_object:
    lines = file_object.read()

print(lines)
'''


#replace text
filename = 'pi_learned.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()
    x = pi_string.replace('text', 'dog')

print(x)
