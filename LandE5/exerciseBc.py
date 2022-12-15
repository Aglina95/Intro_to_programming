# Write your code here :-)
from unittest import result
from xxlimited import foo


def format_list(food):
    result = ""
    # convert the list item by item by adding it to the result variable
    for i in range(len(food)):
        if i > 0:
            if i == len(food) -1:
                result = result + " and "

            else:
                result = result + ", "
        result = result + food[i]
    return result


    #result += food[i]
    #result = result + ", "

food = ['apples', 'bananas', 'tofu', 'pork']

print(format_list(food)) # is supposed to print 'apples, bananas, tofu, and pork'


#or 
#separate with ', ' and 'and'
def format_list(food):
    result = ""

    if len(food) == 0:
        return result
    if len(food) == 1:
        return food[0]

    for item in food[:-1]:
        result += item + ", "
    result += "and " + food[-1]
    return result

food = ['aa', 'aaaaad']
print(format_list(food)) 
