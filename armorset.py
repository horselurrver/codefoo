import csv

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
# takes shopping cart and new item, then replaces item of same category in the inventory
# if two items of same category, replace the more expensive item
# returns a new inventory
def replaceItem(shoppingCart, newItem):
    newCart = shoppingCart
    # mark newItem in inventory --> has been in shopping cart
    if hasTwoOfCategory(newCart, newItem.type):
        # replace the more expensive item
        # by first finding indices of items with the same category as the new item
        itemIndicesWithSameCategory = []
        for index, value in enumerate(newCart):
            if value.type == newItem.type:
                itemIndicesWithSameCategory.append(index)
        index1 = itemIndicesWithSameCategory[0]
        index2 = itemIndicesWithSameCategory[1]
        # now replace the more expensive item
        if newCart[index1].cost > newCart[index2].cost:
            newCart[index1] = newItem
        else:
            newCart[index2] = newItem
    else:
        for index, value in enumerate(newCart):
            if value.type == newItem.type:
                newCart[index] = newItem
    return newCart

# checks if inventory has two of same category items
def hasTwoOfCategory(inventory, category):
    result = []
    for item in inventory:
        if item.type == category:
            result.append(item)
    return len(result) == 2


# given sorted inventory, return next highest value equipment not in shopping cart
def getNext(shoppingCart):
    for item in getNextBestInventory:
        if item in shoppingCart:
            getNextBestInventory.remove(item)
        else:
            result = item
            getNextBestInventory.remove(item)
            return result

# sort array based on value, with item in index 0 having the biggest value
def sortList(array):
    sortedArray = sorted(array, key=lambda x: x.value, reverse=True)
    return sortedArray

# get how many crowns we'll be spending on the current shopping cart
def getTotalCost(shoppingCart):
    total = 0
    for item in shoppingCart:
        total += int(item.cost)
    return total

def getValue(shoppingCart):
    total = 0
    for item in shoppingCart:
        total += int(item.value)
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
                pass
            else:
                type = row[0]
                name = row[1]
                cost = row[2]
                value = int(row[3])
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

budget = 300 # crowns available to purchase equipment
myShoppingCart = []
# load separate inventories for the different equipment
helmet, boots, leggings, chest = loadInventory()
inventory = helmet + boots + leggings + chest
# make an inventory with all items that are sorted by value (descending)
inventory.sort(key=lambda x: x.value)
inventory.reverse()
getNextBestInventory = inventory.copy()

counter = 0
for category in [helmet, boots, leggings, chest]:
    maximum = getNthMax(counter, category)
    myShoppingCart.append(maximum)
    #    add one more item to shopping cart
myShoppingCart.append(getNext(myShoppingCart))

finalShoppingCart = myShoppingCart.copy()
while True:
    if len(getNextBestInventory) == 0:
        break
    if getTotalCost(myShoppingCart) > budget:
        # get item with next best value
        nextItem = getNext(myShoppingCart)
        # replace the item with the same category by next best valued item
        myShoppingCart = replaceItem(myShoppingCart, nextItem)
        finalShoppingCart = myShoppingCart.copy()
    else:
        break

print(str(finalShoppingCart))
cost = getTotalCost(finalShoppingCart)
value = getValue(finalShoppingCart)
print('Cost: ' + str(cost))
print('Value: ' + str(value))
