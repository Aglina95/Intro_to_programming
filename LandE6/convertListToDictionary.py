# Write your code here :-)
def convert(lst):
    res_dictionary = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dictionary

dummy_list = ['a' , 1, 'b', 2]
print(convert(dummy_list))
