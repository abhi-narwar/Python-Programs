# Count the frequency of each character in a string and store it in a dictionary
#string='somese'

class Solution:
    def frequency_count(self,str):
        dict={}
        for i in str:
            if i  in dict:
                dict[i]+=1
            else:
                dict[i]=1
        return dict
s=Solution()
s.frequency_count('somese')
                
            
            
            
            
            
        



