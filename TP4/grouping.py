import os

content = os.listdir('./Resources/input')


for file in content:
    grouping = []
    with open('./Resources/input/' + file, 'r') as reader:
        for line in reader:
            split = line.split(',')
            group = (int(split[0]) // 4) + ((int(split[1])) // 4) * 5
            aux = [split[2], group]
            grouping.append(aux)
        reader.close()

    outF = open(file + 'groups' + '.csv', 'w')
    sortedCountries = sorted(grouping, key=lambda x:x[1])
    for group in sortedCountries:
        country = group[0].split('\n')
        outF.write(str(country[0]) + ',' + str(group[1]))
        outF.write('\n')
    outF.close()

