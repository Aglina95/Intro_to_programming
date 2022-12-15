# Write your code here :-)
import sys
from timeit import default_timer

def sum_to(n):
  s = 0
  for i in range(n + 1):
    s += i
  return s

n = int(sys.argv[1])

start = default_timer()
print(f"The sum of the first {n} numbers is {sum_to(n)}")
print(f"The computation took {default_timer() - start} seconds.")
