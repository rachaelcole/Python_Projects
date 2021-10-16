print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is another name pointing to the same object
mylist = shoplist
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
# mylist makes a copy by doing a full slice
mylist = shoplist[:]
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
