# Write your code here :-)
"""def a(x):
    l = []
    for b in x:
        if b < 0:
            l.append(b)
    return l"""

"""This function checks if int elements of a list are less than 0
and returns a list with these elements (which are less than 0)"""

def append_element(list_of_nums):
    new_list = []

    for element in list_of_nums:
        if element <= 0:
            new_list.append(element)
    return new_list


print(append_element([1, -122, 0]))
print(append_element([1, -122, -1]))
print(append_element([1, 2, 3]))

assert append_element([1, -122, 0]) == [-122, 0]
assert append_element([1, -122, -1]) == [-122, -1]
assert append_element([1, 2, 3]) != [1, 2, 3]


