import csv
from matplotlib import pyplot as plt 

filename = open('UNSW_NB15_training-set.csv', 'r')
file = csv.DictReader(filename)

Spkts = []
sloss = []

a=[None]*20
b=[None]*20

for col in file:
    Spkts.append(col['spkts'])
    sloss.append(col['sloss'])

    
plt.scatter(Spkts, sloss)
plt.show()
    

    