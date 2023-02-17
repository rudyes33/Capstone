import csv
from matplotlib import pyplot as plt 

filename = open('UNSW_NB15_training-set.csv', 'r')
file = csv.DictReader(filename)

Dpkts = []
dloss = []

a=[None]*20
b=[None]*20

for col in file:
    Dpkts.append(col['dpkts'])
    dloss.append(col['dloss'])

for i in range(20):
    a[i]=Dpkts[i]
    b[i]=dloss[i]
    
plt.scatter(Dpkts, dloss)
plt.show()
    

    