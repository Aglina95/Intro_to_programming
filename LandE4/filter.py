def my_predicate(number):
    return number > 3

def is_char_a(char):
    return char == "a"

# Write your code here :-)
def filter(iterable, predicate):
    for item in iterable:
        if predicate(item):

            yield item



join_a = list(filter("angelina", is_char_a))
x = "".join(join_a)
print(x)
assert x == "aa"

