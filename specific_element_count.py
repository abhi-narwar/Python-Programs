#3. Count how many times a specific element appears in a list
class Solution:
    def count_element(self, lst, element):
        count = 0
        for i in lst:
            if i == element:
                count += 1
        return count

s = Solution()
print(s.count_element([1, 2, 3, 2, 4, 2, 5], 2))  

