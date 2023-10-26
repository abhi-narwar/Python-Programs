ls=[]
while True:
    item = input('enter the item name')
    if item == '':
        break
    ls.append(item)
ls.sort()
print(ls)
