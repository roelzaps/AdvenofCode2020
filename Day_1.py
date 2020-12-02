#  find to entries that sum to 2020 and then multiply those number together

import itertools

with open('data.txt','r') as file:
    data = list(map(int,file.read().split()))

comb = itertools.combinations(data, 2)

for i in comb:
    if sum(list(i)) == 2020:
        print(i[0]*i[1])