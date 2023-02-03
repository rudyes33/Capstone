import csv

filename = open('UNSW_NB15_training-set.csv', 'r')
file = csv.DictReader(filename)

sbytes = []
dbytes = []
sload = []
dload = []


for col in file:
    sbytes.append(col['sbytes'])
    dbytes.append(col['state'])
    sload.append(col['sload'])
    dload.append(col['dload'])


    
print(sload)

    