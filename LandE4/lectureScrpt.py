# Write your code here :-)
import sys
#or from sys import stdin
#list is a datatype

previous_name = ' '
counter = 0

for name in sys.stdin:
    name = name.rstrip()
    if previous_name == name:
        counter = counter + 1
    else:
        if counter != 0:
            print('The name ' + previous_name + ' appeared' + str(counter) + ' times')
        previous_name = name
        counter = 1



