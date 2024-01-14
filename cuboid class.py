class cuboid:
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h
    def lidarea(self):
        return self.length*self.breadth
    def volume(self):
        return self.length*self.breadth*self.height
c1=cuboid(10,2,3)
print(c1.volume())



c2=cuboid(2,3,5)
print(c2.lidarea())
