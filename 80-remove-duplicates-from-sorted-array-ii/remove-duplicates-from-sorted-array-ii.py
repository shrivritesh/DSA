class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow = 2

        # for fast in range(2,len(nums)):
        #     if nums[fast] != nums[slow - 2]:
        #         nums[slow] = nums[fast]
        #         slow += 1

        # return slow
            

# using while loop 

        # slow = 2
        # fast =  slow
        slow = fast = 2

        while fast  < len(nums):
            if nums[fast]!= nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
    