#2. Check whether a number is a palindrome or not

class Solution:
    def is_palindrome(self, num):
        original = num
        rev = 0
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10
        return rev == original

s = Solution()
print(s.is_palindrome(121))  
