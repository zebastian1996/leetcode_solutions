
nums = [1,1,2]
#nums = [0,0,1,1,1,2,2,3,3,4]

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
a = 0
for i in nums:
    if i != nums[a]:
        nums[a+1] = i
        a += 1
print(nums)

####leetcode svaret
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         resultat=[nums[0]]
#         a = 0
                
#         for i in nums:
#             if i != nums[a]:
#                 nums[a+1] = i
#                 a += 1
#         return a+1