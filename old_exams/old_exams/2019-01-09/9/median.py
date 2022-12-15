def median(L):
    while len(L) > 1:
        MIN = min(L)
        MAX = max(L)
        L.remove(MIN)
        L.remove(MAX)
    return L[0]

print (median([1,3,-1,10,11]))

