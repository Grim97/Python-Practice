import sys

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i, j
                else:
                    continue

    
def main():
    objec = Solution()
    print(objec.twosum(sys.argv[1], sys.argv[2]))
    

if "__name__" == "__main__":
    main()