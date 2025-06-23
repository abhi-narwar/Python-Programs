#cumulative sum

#arr=[1,2,3,4]    out=[1,3,6,10]
def cumulative_sum(arr):
    for i in range(1,len(arr)):
        arr[i]=arr[i]+arr[i-1]
    return arr
arr=[1,2,3,4]
print(cumulative_sum(arr))

#[1,3,6,10]

        
        

        
        
        
    
            
            
        
    
    
