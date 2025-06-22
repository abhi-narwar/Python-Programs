# Create a list of numbers from 1 to 100 that are divisible by both 3 and 5

class Solution:
    def create_list(self):
        lst=[]
        for i in range(1,101):
            if i%3==0 and i%5==0:
                lst.append(i)
        return lst
s=Solution()
print(s.create_list())
        

