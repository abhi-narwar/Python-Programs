marks={'physics':3,
       'english':2,
       'math':1,
       'webtech':5,
       'python':None}

s=0
for i in marks:
    val=marks[i]
    if type(val)==int:
        s += val
print('total Marks',s)
