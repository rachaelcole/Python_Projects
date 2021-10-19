inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print('Total number of items:', item_total)
    print('')


def add_to_inventory(inventory, items_added):
    for i in range(len(items_added)):
        if items_added[i] in inventory:
            inventory[items_added[i]] += 1
        else:
            inventory[items_added[i]] = 1
    print('Added to inventory:')
    for i in range(len(items_added)):
        print(items_added[i])
    print('')


display_inventory(inventory)
add_to_inventory(inventory, added_items)
display_inventory(inventory)
