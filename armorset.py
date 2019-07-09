import csv

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

budget = 300 # crowns available to purchase equipment
myShoppingCart = []
# load separate inventories for the different equipment
helmet, boots, leggings, chest = loadInventory()
inventory = helmet + boots + leggings + chest
# make an inventory with all items that are sorted by value
inventory = sortList(inventory)

for category in [helmet, boots, leggings, chest]:
    maximum = getNthMax(0, category)
    myShoppingCart.append(maximum)
# add one more item to shopping cart


cost = getTotalCost(myShoppingCart)
print('My shopping cart: ' + str(myShoppingCart))
print('Cost: ' + str(cost))
