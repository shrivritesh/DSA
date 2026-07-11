class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sort_nums = sorted(nums)

        dic = {}

        for i ,num in enumerate(sort_nums):
            if num not in dic:
                dic[num] = i

        res = []

        for i in nums:
            res.append(dic[i])

        return res