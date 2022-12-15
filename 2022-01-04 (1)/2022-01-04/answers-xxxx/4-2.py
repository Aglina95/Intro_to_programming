def f(L):
    s = 0
    x = L[0]
    while x > 0:
        s = s + x
        break

    return s

L = [2]
print(f(L))

assert f([2]) == 2
assert f([3]) != 2

#if you don't remember how to write a method, put the text from the exercise description to indicate what this method should do
#by opening files you also get points
#They ver ask for constant, linear or logarithmic when asking about difficult
