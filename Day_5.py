# there 10 character ex 'FBFBBFFRLR'
# the first 7 char will be either 'F' or 'B' and specify exactly one the 128 rows of the plane(number 0 to 127)
# each letter tells me which half of the region the given seat is in
# the first letter indicates wheather the seat is in front( 0 to 63) or Back(64 to 127)
# the next letter indicates which half of that region the seat is in, and so on until you're lesft with exactly one row.

# the last three letter will be eirther 'L' or 'R'
# the specify exactly one of the 8 columns of seats on the plane( 0 to 7).
# 'L' means keep the lower part.
# 'R' means keep the upper part.

# seats has a seat unique ID = row * 8 + column

# Part 1 Find the hieghest Seat ID on the boarding pass.

#this will load the data file in the directory
with open('data5.txt', 'r') as file:
    data = file.read().splitlines()
#create a row and column list of number
row_num = [i for i in range(0,128)]
col_num = [i for i in range(0,8)]
#create a function will decode the letters on boarding pass. return the row and column number of the seet
def seat_number(code):
    row_n = row_num
    col_n = col_num
    for i in code:
        if i == 'F':
            row_n = row_n[:len(row_n)//2]
        if i == 'B':
            row_n = row_n[len(row_n)//2:]
        if i == 'R':
            col_n = col_n[len(col_n)//2:]
        if i == 'L':
            col_n = col_n[:len(col_n)//2]
    return row_n[0], col_n[0]

seats = list(map(seat_number,data))
seat_id = sorted(list(map(lambda r: r[0] * 8 + r[1], seats)))

# Part 1 answer
print('the Max Seat id is ', max(seat_id))


# Part 2
seat_range = [*range(seat_id[0],seat_id[len(seat_id)-1]+1)]
my_seat_id = list(set(seat_range) - set(seat_id))
print(f'My Seat Id is {my_seat_id[0]}')