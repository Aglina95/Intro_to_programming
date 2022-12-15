# Write your code here :-)
from timeit import default_timer


def has_element(elem, data):
    #checks whether 'elem' is in 'data'.
    #Assume that data has N elements
    for e in data: #Do N iterations of the for loop
        if e == elem: #for each iteration, I check this once
            return True #For each if that was true, I do this onece

        return False

assert has_element(3, [1, 2, 3])
assert has_element("3", [1,2,3]) == False

assert 3 in [1,2,3] #"in" is doing the same as has_element

#O(N) linear in the size of the list

data = [i for i in range(200_000_000_000)]
print(data[:10])

start = default_timer()
has_element_bin(-1, data)
print(f'It took {default_timer() - start}s to search for -1')
