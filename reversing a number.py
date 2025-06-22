#9. Take a number input and print its reverse
class Solution:
    def reverse(self,num):
        rev=0
        while num!=0:
            r=num%10
            num=num//10
            rev=rev*10+r
        return rev
           
        
         
        
     
s=Solution()
print(s.reverse(123))
