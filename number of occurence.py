L1=['a','b','c','d','a','c','e','f','g','h','h','i']

result=[]

for x in L1:
    if x not in result:
        result.append(x)
        count=L1.count(x)
        result.append(count)

print(result)
  
