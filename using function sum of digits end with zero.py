def sum0(L):
    sum=0
    for i in L:
        if i%70==0:
            sum+=i

    return sum
L=[200,345,300,567]
print(sum0(L))

     
