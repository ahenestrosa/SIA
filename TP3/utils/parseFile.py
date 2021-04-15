import numpy as np
import csv

def parseFile(filename):
    f = open(filename, 'r')
    reader = csv.reader(f, delimiter=' ')
    data = []
    for row in reader:
        clean_row = [float(i) for i in row if i != '']
        if len(clean_row) == 1:
            data.append(clean_row[0]) 
        elif len(clean_row) > 1:
            data.append(clean_row)   

    return np.array(data)
    