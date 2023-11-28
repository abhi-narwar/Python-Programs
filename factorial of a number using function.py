def factorial(n):
    i=1
    for r in range(1,n+1):
        i*=r
    return r

dct={}
while 1:
    num=int(input("enter the number"))
    out=factorial(num)
    print(f'factorial of given number {num} is {out}')
    dct[num]=out
    print('do you want contribiute y/n')
    if input() != 'y':
          print(f'your all result {dct}')
          break
