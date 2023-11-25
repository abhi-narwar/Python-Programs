def is_palindrome(s):
    return s == s[::-1]


my_string = input('enter the string')
result = is_palindrome(my_string)

print(result)
