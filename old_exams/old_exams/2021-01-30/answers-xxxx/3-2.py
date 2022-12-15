def f(L):
    n = len(L)
    i = 0
    cnt = 0

    while i < n:
        if L[i] < 0:
            cnt = cnt + 1
        i = i + 1
    return cnt
