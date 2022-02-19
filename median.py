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
    newData.sort()
    print(n)
    
    if n % 2 == 0:
        median1 = float(newData[n//2])
        median2 = float(newData[n//2 - 1])
        median = (median1 + median2)/2
    else:
        median = newData[n//2]

    print(median)