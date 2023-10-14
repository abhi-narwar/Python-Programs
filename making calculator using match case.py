num1=int(input('enter the number1:'))
num2=int(input('enter the number2:'))
operator=input('operator')
match operator:
    case'+':
        print('sum is',num1+num2)
    case'-':
        print('difference is',num1-num2)
    case'%':
        print('remainder is',num%num2)
    case'/':
        print('quotient is',num1/num2)

    


