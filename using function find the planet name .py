def planet(id):
    planet={1:'mercury',2:'venus',3:'jupiter',4:'sun'}
    return planet[id]
id=int(input("enter the id of planet"))
c=planet(id)
print(c)  
