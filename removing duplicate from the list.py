l1=[1,2,3,4,3,2,8]

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
