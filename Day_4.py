# i need to check if the all the eight fields in passport are present (ecl,gry,pid, eyr, hcl, byr, iyr, cid, hgt). 
#each field is reprent key:value
#i need to laod the data as list of dictionary

from voluptuous import Schema, Optional, Match


with open('data4.txt', 'r') as file:
    data = file.read().split('\n\n')

#create a list of dictionary. where the dictionary contains the information a passport
passport_details = []
for i in range(0,len(data)):
    passport_details.append(dict(map(lambda x: x.split(':'),data[i].split())))    

#Part 1 solution validate the passport
count = 0
valid_passport =[]
for i in range(0,len(passport_details)):
   if 'byr' in list(passport_details[i].keys()) and 'iyr' in list(passport_details[i].keys()) and 'eyr' in list(passport_details[i].keys()) and \
        'hgt' in list(passport_details[i].keys()) and 'hcl' in list(passport_details[i].keys()) and 'ecl' in  list(passport_details[i].keys()) \
            and 'pid' in list(passport_details[i].keys()):
        count += 1
        valid_passport.append(passport_details[i])
print(f'there are {count} valid passport base on the fields criteria')

#Part 2 solution validate the passport
schema = Schema({'byr': Match(r'^19[2-9][0-9]$|^200[0-2]$'), 
                 'iyr': Match(r'^201[0-9]$|^2020$'),
                 'eyr': Match(r'^202[0-9]$|^2030$'),
                 'hgt': Match(r'^1[5-8][0-9]cm$|^19[0-3]cm$|^59in|[6][0-9]in$|^7[0-6]in$'),
                 'hcl': Match(r'^#[0-9a-f]{6}$'),
                 'ecl': Match(r'^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$'),
                 'pid': Match(r'^[0-9]{9}$'),
                  Optional('cid') : str 
                })
count2 = 0
not_valid = []
for i in range(0,len(valid_passport)):
    try:
        if schema(valid_passport[i]):
            count2 += 1
            
    except:
        continue
print(f'there are {count2} valid passport base on field values')