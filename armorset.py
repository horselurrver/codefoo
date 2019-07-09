import csv

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

# Define class item for each item in the inventory
class Item:
    def __init__(self, type, name, cost, value):
        self.type = type
        self.name = name
        self.cost = cost
        self.value = value
    def getType(self):
        return self.type
    def getName(self):
        return self.name
    def getCost(self):
        return self.cost
    def getValue(self):
        return self.value
    def __repr__(self):
        return '[{}, {}, {}, {}]'.format(self.type, self.name, self.cost, self.value)

budget = 300 # crowns available to purchase equipment

helmet, boots, leggings, chest = loadInventory()
print(max(helm.value for helm in helmet))
