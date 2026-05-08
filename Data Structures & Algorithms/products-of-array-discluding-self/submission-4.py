class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = []

        for x in nums:
            ans.append(prefix)
            prefix *= x
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            x = nums[i]
            suffix *= x
        
        return ans