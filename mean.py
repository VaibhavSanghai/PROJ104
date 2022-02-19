import csv
from collections import Counter

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

    file_data.pop(0)
    newData = []

    for i in range(len(file_data)):
        nNo = file_data[i][1]
        newData.append(float(nNo))
    
    n = len(newData)
    total = 0
    for v in newData:
        total += v
    mean2 = total/n
    print(mean2)