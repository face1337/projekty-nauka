inventory = {'rope': 1, 'torch': 6, 'dagger': 1, 'gold coin': 42, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

new_inventory = {}


def display_inventory(inv):
    print('Inventory : ')
    total_items = 0
    for items in inv:
        print(inv[items], items)
        total_items += inv[items]
    print('Total number of items in your inventory: ' + str(total_items))


def add_to_inventory(inv, added_items):
    for item in added_items:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1
    return inv


inventory = add_to_inventory(new_inventory, dragonLoot)
display_inventory(new_inventory)
