L1=[[2,3,4],[5,5,5],[6,7,8]]
L2=[[2,3,4],[5,5,5],[6,7,8]]
L3=[]
for i in range(3):
    s=[]
    for j in range(3):
       r=L1[i][j]+L2[i][j]
       s.append(r)
    L3.append(s)
print(L3)
   
