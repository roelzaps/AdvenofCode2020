# Part 1:  find to entries that sum to 2020 and then multiply those number together
# Part 2: find the product of three entries that sum to 2020

import itertools
import numpy as np

with open('data.txt','r') as file:
    data = list(map(int,file.read().split()))

def productcomb(itemlist, numcomb):
    comb = itertools.combinations(itemlist, numcomb)
    for i in comb:
        if sum(list(i)) == 2020:
            print(np.prod(i))


# Part 1 solution
productcomb(data, 2)

# Part 2 solution
productcomb(data,3)