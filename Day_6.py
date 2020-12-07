from functools import reduce

with open('data6.txt', 'r') as file:
    data = file.read().split('\n\n')

#Part 1 solution
# convert to sets
list_set = list(map(set,data))
#remove '\n'
def remove_n(x):
    a =  x - {'\n'}
    return len(a)
list_set2 = list(map(remove_n,list_set))
print(sum(list_set2))

#Part 2 solution
# group the group as list.
group_list = list(map(lambda x : x.split('\n'), data))
group_list_set = []
for i in group_list:
    group_list_set.append(list(map(set,i)))

count = []
for sets in group_list_set:
    yes_answer = reduce(set.intersection, sets)
    count.append(len(yes_answer))
print(sum(count))
