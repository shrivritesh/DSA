class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)

        # want = n * (n + 1) // 2
        # actual = sum(nums)
        # return want - actual

        # def miss_num(numbers):

        return sum(range(len(nums) + 1)) - sum(nums)