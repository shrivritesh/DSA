# Ques: 80
# Remove Duplicate from sorted array ||
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:


def remove_duplicate(nums):
    slow = 2
    fast = len(nums) - 2

    while fast < len(nums):
        if nums[fast]!= nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    
    return slow

num = int(input("Inter Array :"))

print(remove_duplicate(num))
