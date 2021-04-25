import numpy as np
import csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


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
    
 
def readAndNormalize(trainingSetPath, resultSetPath):
    file1 = trainingSetPath
    file2 = resultSetPath
    trainingSet = open(file1, "r")
    resultSet = open(file2, "r")

    x = []
    y = []
    z = []
    results = []

    for l in resultSet:
        line = l.split()
        results.append(float(line[0]))

    for l in trainingSet:
        line = l.split()
        x.append(float(line[0]))
        y.append(float(line[1]))
        z.append(float(line[2]))

    data = pd.DataFrame({ 'x':x, 'y':y, 'z':z, 'res':results})

    min_val_training = [min(x), min(y), min(z)]
    max_val_training = [max(x), max(y), max(z)]
    min_val_expected = min(results)
    max_val_expected = max(results)


    x_normalized = []
    for i in x:
        value = float(i)
        x_normalized.append( (2*(value - min_val_training[0])/(max_val_training[0] - min_val_training[0]) - 1))
    
    y_normalized = []
    for i in y:
        value = float(i)
        y_normalized.append( (2*(value - min_val_training[1])/(max_val_training[1] - min_val_training[1]) - 1))

    z_normalized = []
    for i in z:
        value = float(i)
        z_normalized.append( (2*(value - min_val_training[2])/(max_val_training[2] - min_val_training[2]) - 1))
    
    r = []
    for i in results:
        value = float(i)
        r.append( (2*(value - min_val_expected)/(max_val_expected - min_val_expected) - 1))
        
    normalized = pd.DataFrame({ 'x':x_normalized, 'y':y_normalized, 'z':z_normalized, 'r':r})
    normalized = normalized.values
    normalized
    return normalized

