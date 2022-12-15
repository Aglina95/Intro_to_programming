# Write your code here :-)
import sys
from turtle import right

#for idx, argument in enumerate(sys.argv):
    #if idx == 0:
        #continue
    #print(idx, argument)

counter = 0

for idx, argument in enumerate(sys.argv):
    print(idx)
    print(counter)

    counter = counter + 1


def newenum(iterable):
    index = 0
    for item in iterable:
        yield (index, item)
        index += 1
