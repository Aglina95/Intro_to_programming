# Write your code here :-)
import sys

all_names = []

for name in sys.stdin:
    name = name.rstrip()
    all_names.append(name)

print(all_names) #print the whole list
print(all_names[0]) #print the first element
print(all_names[-10:]) #print the last 10 names

unique_names = []

for names in all_names:
    if name not in unique_names:
        unique_names.append(name)
print(len(unique_names))
