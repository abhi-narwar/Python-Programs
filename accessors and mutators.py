class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def getlength(self):
        return self.length
    def setlength(self,l):
        self.length=l
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
r=rectangle(10,5)
print(r.getlength())
print(r.setlength(15))
print(r.area())
print(r.perimeter())


        
