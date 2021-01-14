
import csv

D = {"math":{}, "phy":{}, "chem":{}}
B = 0

def updateDictByField(D, city, mark, subjectParam):
    if city in D[subjectParam].keys():
        if D[subjectParam][city] < mark:
            D[subjectParam][city] = mark
    else:
        D[subjectParam][city] = mark
    return D
    pass

def eligible(D, town, mark):
    sublist = ["math", "phy", "chem"]
    c= 0
    for sub in sublist:
        if D[sub][town] == mark[sub]:
            c = c+1
    return c

with open('marks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            D = updateDictByField(D, row[0].lower(), row[1], "math")
            D = updateDictByField(D, row[0].lower(), row[2], "phy")
            D = updateDictByField(D, row[0].lower(), row[3], "chem")
            line_count += 1

with open('marks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if eligible(D, row[0].lower(), {"math": row[1], "phy":row[2], "chem":row[3]}) > 1:
                B =B +1

print(D)
print(B)