inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Write function here
def display_inventory(inventory):
    space = " "
    print("Inventory:")

    inventory_items = sorted(inventory.items())


    for key, value in inventory_items:
        print(f'{value}{space}{key}')

display_inventory(inventory) # this has to work and produce the output from above


'''Write a function named display_inventory that would take any possible “inventory” and display it like the following

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62'''
