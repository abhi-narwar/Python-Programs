from random import*
c_num=randrange(1,101)
while 1:
    u_num=int(input())
    if u_num == c_num:
        print("you win")
        break
    elif u_num>c_num:
        print("too large")
    else:
        print("too small")

