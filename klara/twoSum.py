
nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                summa = nums[i]+nums[j]
                if summa == target and j != i:
                    svaret = [i,j]
        return svaret
    
lösning = Solution()
print(lösning.twoSum(nums,target))