class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #    create a set of nums
        numSet = set(nums)
        ans = 0

        for n in nums:
            # check if n is the starting of the sequence, if not, ignore it/skip it
            if (n-1) not in nums: 
                length = 0
                while n + length in nums:
                    length += 1
                
                ans = max(ans, length)

        return ans