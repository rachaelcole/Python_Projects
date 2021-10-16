# This is a string object
name = 'Rachael'

if name.startswith('Rac'):
    print('Yes, the string starts with "Rac"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('cha') != 1:
    print('Yes, it contains the string "cha"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
