# write a program that prints the item that has been sold most frequently.

sold = {}
with open('sales.txt') as f:
    for line in f:
        sold.setdefault(line, 0)
        sold[line] += 1
print(max(sold, key=sold.get))





