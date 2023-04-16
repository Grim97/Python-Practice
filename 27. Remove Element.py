class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1

        k = len(nums)
        return k


'''
Don't rely on for loop with range function. With range you cannot modify index value inside the loop. Use while, where you have control over the index modifications.
'''

# nums = [int(x) for x in input().strip('[]').split(',')]
# val = int(input())
# obj = Solution()
# obj.removeElement(nums, val)
