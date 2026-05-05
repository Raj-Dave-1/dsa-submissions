class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = { nums[i] : i for i in range(len(nums)) }

        for i, num in enumerate(nums):
            diff = target - num
            if diff in d and d[diff] != i:
                return [i, d[diff]]

