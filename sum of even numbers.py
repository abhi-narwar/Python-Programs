#4. Sum of Even Numbers:
 #Write a program that calculates the sum of all even numbers from 1 to n, where n is an integer 
#input by the user, using a while loop

n=int(input("enter the number"))
sum=0
i=1

while i<=n:
    if i%2==0:
      sum =sum+i
    i=i+1
print(sum)




