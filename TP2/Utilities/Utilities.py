from Utilities import Constants

def itemParse(filePath):

    items = {}
    lineNum = 0
    with open(filePath, 'r') as reader:
        # Read and print the entire file line by line
        for line in reader:
            print()
            if lineNum != 0:
                newItem = {}
                split = line.split('\t')
                newItem[Constants.FUERZA] = float(split[1])
                newItem[Constants.AGILIDAD] = float(split[2])
                newItem[Constants.PERICIA] = float(split[3])
                newItem[Constants.RESISTENCIA] = float(split[4])
                newItem[Constants.VIDA] = float(split[5])
                newItem[Constants.ID] = int(split[0])
                items[split[0]] = newItem
            else:
                lineNum += 1
    return items

def findItem(filePath, id):
    item = {}
    found = False
    with open(filePath, 'r') as reader:
        for line in reader:
            split = line.split('\t')
            if split[0] == str(id):
                item[Constants.FUERZA] = float(split[1])
                item[Constants.AGILIDAD] = float(split[2])
                item[Constants.PERICIA] = float(split[3])
                item[Constants.RESISTENCIA] = float(split[4])
                item[Constants.VIDA] = float(split[5])
                item[Constants.ID] = int(split[0])
                found = True
            elif found == True:
                return item

    return item
