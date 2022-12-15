# Write your code here :-)
#try and play around by creating a list and print a
#this code checks if the elements of a list are the same
a = True
L = [1,2,1]
for x in L:
    for y in L:
        if x != y:
            a = False

print(a)
#prints false, therefore the elements of the list are not the same
