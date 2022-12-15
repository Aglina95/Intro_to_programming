# Write your code here :-)
import sys

#argvlist = sys.argv[1:]
#[int(element) for element in sys.argv[1:]] Creates new list with int elements.

first_element = sys.argv[1] #access the second element(the 1st is the name of the program)

int_elem = int(first_element) #element from str to int

int_elem += 1 #increment

print(int_elem)



#print(argvlist[0])
