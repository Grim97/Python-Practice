import sys

class Solution:
    def isPalindrome(self, x):
        y = str(x)
        if y == y[::-1]:
            return True
        else:
            return False
        
        
obj = Solution()
inval = sys.argv[1]
# print(inval)
# inval = input()
print(obj.isPalindrome(inval))