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

data = Counter(newData)
mode_data_for_range = {"50-60": 0, "60-70": 0, "70-80": 0}

for height, occurance in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurance
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurance
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurance

moderange, modeoccurance = 0, 0
for range, occurance in mode_data_for_range.items():
    if occurance > modeoccurance:
        moderange, modeoccurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance
mode = float((moderange[0] + moderange[1])/2)
print(mode)