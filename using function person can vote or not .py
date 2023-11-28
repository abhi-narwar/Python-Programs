def vote(age):
    if age > 18:
        return "can vote"
    else:
        return "can not vote"
age=int(input("enter the age "))
d=vote(age)
print(d)
