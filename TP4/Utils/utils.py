import csv

def parseFile(filename):
    f = open(filename, 'r')
    reader = csv.reader(f, delimiter=',')
    names = []
    matrix = []
    header = True
    for row in reader:
        if header == True:
            header = False
        else:
            names.append(row[0])
            matrix.append(row[1:])

    return names, matrix