food=['apple','banana','mango','sweet','burger','tinkercad']
letter=input('enter the letter')
for i in food:
    if i.startswith(letter):
        print(i)
