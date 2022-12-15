# Write your code here :-)

#inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

total_items = 0
# Write function here
def display_inventory(inventory_set):
    print("Inventory:")
    for k,v in sorted(inventory_set.items()):  #sorted() for sorting the set alphabetically

        print(v,k)

def add_to_inventory(inventory, added_items):

    for i in added_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', "arrow"]
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
