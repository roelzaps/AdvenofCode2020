
with open('./data3.txt', 'r') as file:
    maps = file.read().splitlines()


maps2 = list(map(lambda x: x*(int(len(maps)/3)), maps ))


def map_slopes(right_slope, down_slope):
    right = 0
    down = 0
    tree_count = 0
    while True:
        try:
            right += right_slope
            down += down_slope
            if maps2[down][right] == '#':
                tree_count += 1
        except:
            return tree_count

#part 1 solutions
print(f'there are {map_slopes(3,1)} of tree\'s ')

#part 2 solutions
print(f'the product of slope given slope is {map_slopes(1,1)*map_slopes(3,1)*map_slopes(5,1)*map_slopes(7,1)*map_slopes(1,2)}')