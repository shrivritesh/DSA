class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
    #    return len(nums) != len(set(nums))
        if len(set(nums)) != len(nums):
            return True
        return False


