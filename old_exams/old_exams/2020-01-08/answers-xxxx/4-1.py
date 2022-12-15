def double_list_elements(other_list):
    i = 0
    while i < len(other_list):
    other_list[i] = other_list * 2
    i = i - 1

my_list = [1, 3, 5]
double_list_elements(my_list)
print(my_list) # should print [2, 6, 10]
