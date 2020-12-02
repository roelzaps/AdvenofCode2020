# Part 1 determine how many password are valid with the given data with password policy and a password.
# password policy is number of times letter should appear.


with open('data2.txt', 'r') as file:
    data = file.read().splitlines()

    
valid_pass = []
valid_pass2 = []
for i in data:
    split1 = i.split(': ')
    password = split1[1]
    split2 = split1[0].split()
    split3 = split2[0].split('-')
    letter = split2[1]
    min_num = int(split3[0])
    max_num = int(split3[1])
    #Part 1 solution
    if password.count(letter) >= min_num and password.count(letter) <= max_num:
        valid_pass.append(password)

    #part 2 solution
    if (password[min_num-1] == letter or password[max_num-1] == letter) and not(password[min_num-1] == letter and password[max_num-1] == letter): 
        valid_pass2.append(password)
    
print('there are ',len(valid_pass), ' valid password')
print('there are ',len(valid_pass2),' valid password for new policy' )
