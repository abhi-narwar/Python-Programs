list1=[1,3,6,7,8,4]
list2=[1,2,3,6,9,4]

list3=[]

for x in list1:
    if x in list2:
        list3.append(x)
print(list3)
