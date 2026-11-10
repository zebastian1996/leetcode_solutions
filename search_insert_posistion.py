#case1 target = 5 så output = 2
#case2 target = 2 så output = 1
#case3 target = 7 så output = 4
nums = [1,3,5,6]


target = 5
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        
        for i in range(len(nums)):
            if i != target:
                print(i)

lösning = Solution()
print(lösning.searchInsert(nums,target))