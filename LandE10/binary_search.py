# Write your code here :-)

#logarithm 2exp(x) = N
#log(N)
def has_element_bin(elem, data):
    lo = 0
    hi = len(data) - 1
    while lo <= hi:
        mid = (lo + hi) //2
