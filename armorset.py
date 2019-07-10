import csv

# takes shopping cart and new item, then replaces item of same category in the inventory
# if two items of same category, replace the more expensive item
# returns a new inventory
def replaceItem(shoppingCart, newItem):
    newInventory = inventory
    if hasTwoOfCategory(inventory, newItem.type):
        print('Two of category')
        # replace the more expensive item
        # by first finding indices of items with the same category as the new item
        itemIndicesWithSameCategory = []
        for index, value in enumerate(inventory):
            if value.type == newItem.type:
                itemIndicesWithSameCategory.append(index)
        index1 = itemIndicesWithSameCategory[0]
        index2 = itemIndicesWithSameCategory[1]
        # now replace the more expensive item
        if inventory[index1].cost > inventory[index2].cost:
            inventory[index1] = newItem
        else:
            inventory[index2] = newItem
    else:
        print('Only one of category')
        for index, value in enumerate(newInventory):
            if value.type == newItem.type:
                newInventory[index] = newItem
    print('New inventory: ' + str(newInventory))
    return newInventory

# checks if inventory has two of same category items
def hasTwoOfCategory(inventory, category):
    result = []
    for item in inventory:
        if item.type == category:
            result.append(item)
    return len(result) == 2

# given sorted inventory, return next highest value equipment not in shopping cart
def getNextBest(inventory, shoppingCart):
    for i in range(len(inventory)):
        if inventory[i] not in shoppingCart:
            return inventory[i]

# sort array based on value, with item in index 0 having the biggest value
def sortList(array):
    sortedArray = sorted(array, key=lambda x: x.value, reverse=True)
    return sortedArray

# get how many crowns we'll be spending on the current shopping cart
def getTotalCost(shoppingCart):
    print('Shopping cart: ' + str(shoppingCart))
    total = 0
    for item in shoppingCart:
        print('Item cost: ' + str(item.cost))
        total += int(item.cost)
    return total

# get the nth max object from array (check the value)
# if n = 0, get the object with the biggest value
def getNthMax(n, array):
    sorted = sortList(array)
    try:
        result = sorted[n]
        return result
    except IndexError:
        print('Improper index!')

# load inventory from json file into a list
def loadInventory():
    helmet = []
    boots = []
    leggings = []
    chest = []
    with open('inventory.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(' '.join(row))
                pass
            else:
                type = row[0]
                name = row[1]
                cost = row[2]
                value = row[3]
                # print(f'{type}, {name}, {cost}, {value}')
                item = Item(type, name, cost, value)
                if type == 'Helmet':
                    helmet.append(item)
                elif type == 'Boots':
                    boots.append(item)
                elif type == 'Leggings':
                    leggings.append(item)
                else:
                    chest.append(item)
            line_count += 1
    return [helmet, boots, leggings, chest]

# define class item for each item in the inventory
class Item:
    def __init__(self, type, name, cost, value):
        self.type = type
        self.name = name
        self.cost = cost
        self.value = value
    def __repr__(self):
        return '[{}, {}, Cost: {}, Value: {}]'.format(self.type, self.name, self.cost, self.value)

budget = 200 # crowns available to purchase equipment
myShoppingCart = []
# load separate inventories for the different equipment
helmet, boots, leggings, chest = loadInventory()
inventory = helmet + boots + leggings + chest
# make an inventory with all items that are sorted by value
inventory = sortList(inventory)

"""
Algorithm for optimizing:
while True:
    Get maximum of each category plus next highest value not in shopping cart
    If over budget,
        Get the next highest value in the inventory
        Check the category and replace the item in the shopping cart with same category
    If there are two items of the same category in the shopping cart, replace the more expensive item
    else
            break!
"""
counter = 0
for category in [helmet, boots, leggings, chest]:
    maximum = getNthMax(counter, category)
    myShoppingCart.append(maximum)
    #    add one more item to shopping cart
myShoppingCart.append(getNextBest(inventory, myShoppingCart))
print('My shopping cart: ' + str(myShoppingCart))
while True:
    print('Total cost: ' + str(getTotalCost(myShoppingCart)))
    if getTotalCost(myShoppingCart) > budget:
        # get item with next best value
        nextItem = getNextBest(inventory, myShoppingCart)
        print('The next best item: ' + str(nextItem))
        # replace the item with the same category by next best valued item
        myShoppingCart = replaceItem(myShoppingCart, nextItem)
    else:
        break

cost = getTotalCost(myShoppingCart)
print('My shopping cart: ' + str(myShoppingCart))
print('Cost: ' + str(cost))
