def invert(d):
    newd={}
    for a,b in d.items():
        newd[b]=a
    return newd
d1={'a':10,'b':20,'c':30}
print(invert(d1))
        
