from  Paint import Graph

reference_dataSet = []
dataSet1 = [0, 0, 1, 2, 1, 2, 4, 2, 14, 14, 0, 5, 5, 10, 9, 8, 7, 6, 2, 4, 11, 11, 14, 5, 6, 6, 5, 13,
            12, 8, 9, 4, 7, 1, 3, 4, 5, 7, 13, 3, 6, 9, 8, 5, 9, 12, 6, 10, 11, 13]
dataSet2 = [0, 14, 13, 1, 2, 10, 11, 12, 14, 6, 4, 5, 8, 9, 0, 5, 12, 1, 4, 11, 14, 5, 6, 10, 13,
            2, 8, 9, 6, 7, 0, 1, 2, 4, 5, 7, 12, 14, 6, 5, 9, 8, 5, 1, 0, 6, 10, 11, 13, 14]
dataSet3 = [0, 0, 1, 2, 1, 2, 0, 5, 5, 5, 6, 7, 7, 10, 6, 8, 8, 9, 10, 10, 11, 11, 14, 14, 12, 13, 0, 13,
            12, 9, 9, 10, 10, 1, 2, 3, 4, 5, 7, 13, 3, 10, 9, 9, 5, 9, 12, 6, 6, 6]
reference_dataSet.append(dataSet1)
reference_dataSet.append(dataSet2)
reference_dataSet.append(dataSet3)

def FIFO(table_size, dataset):
    time_of_pageFault = 0
    table = []

    for i in range(0, table_size):
        table.append(-1)

    for index in range(0, len(dataset)):
        found = False
        for j in range(0, table_size):
            if table[j] == -1:
                found = True
                time_of_pageFault += 1
                table[j] = dataset[index]
                break
            if table[j] == dataset[index]:
                found = True
                break
        if not found:
            time_of_pageFault += 1
            table.pop(0)
            table.append(dataset[index])
    return time_of_pageFault

def Optimal(table_size, dataset):
    time_of_pageFault = 0
    table = []

    for i in range(0, table_size):
        table.append(-1)

    for index in range(0, len(dataset)):
        found = False
        for j in range(0, table_size):
            if table[j] == -1:
                found = True
                time_of_pageFault += 1
                table[j] = dataset[index]
                break
            if table[j] == dataset[index]:
                found = True
                break
        if not found:
            time_of_pageFault += 1
            maxLenge = 0
            point = 0
            for vimp in range(0, table_size):
                count = 0
                for ref in range(index, len(dataset)):
                    if table[vimp] == dataset[ref]:
                        break
                    else:
                        count += 1
                if count > maxLenge:
                    point = vimp
                    maxLenge = count
            table[point] = dataset[index]
    return time_of_pageFault

def LRU(table_size, dataset):
    time_of_pageFault = 0
    table = []

    for i in range(0, table_size):
        table.append(-1)

    for index in range(0, len(dataset)):
        found = False
        for j in range(0, table_size):
            if table[j] == -1:
                found = True
                time_of_pageFault += 1
                table[j] = dataset[index]
                break
            if table[j] == dataset[index]:
                found = True
                break
        if not found:
            time_of_pageFault += 1
            maxLenge = 0
            point = 0
            for vimp in range(0, table_size):
                count = 0
                for ref in range(1, index + 1):
                    if table[vimp] == dataset[index - ref]:
                        break
                    else:
                        count += 1
                if count > maxLenge:
                    maxLenge = count
                    point = vimp
            table[point] = dataset[index]
    return time_of_pageFault

lineSet = []
for i in range(0, 3):
    line = [0, 0, 0]
    for j in range(3, 11):
        line.append(LRU(j, reference_dataSet[i]))
    print(line)
    lineSet.append(line)

draw = Graph
draw.graph(lineSet, "LRUx")
