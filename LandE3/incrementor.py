# Write your code here :-)
import sys
counter = 0

previous_name = " "

for name in sys.stdin:
    name = name.rstrip()
    if previous_name == name:
        counter = counter + 1
    else:
        if counter != 0:
        print("The name " + previous_name + " appeared" + str(counter) + " times")
        previous_name = name
        counter = 1


    if previous_name != name:
        print("The name " + previous_name + " appeared" + str(counter) + " times")
        previous_name = name
        counter = 1

#print("There are " + str(counter) + " name")
