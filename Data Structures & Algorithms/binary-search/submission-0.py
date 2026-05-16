class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = int((l + r) / 2)
            val = nums[mid]

            if target == val: 
                return mid
            
            if target > val:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1