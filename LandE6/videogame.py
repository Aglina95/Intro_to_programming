# Write your code here :-)
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

total_items = 0
# Write function here
def display_inventory(inventory_set):
    print("Inventory:")
    for k,v in sorted(inventory_set.items()):  #sorted() for sorting the set alphabetically

        print(v,k)

display_inventory(inventory) # this has to work and produce the output from above
