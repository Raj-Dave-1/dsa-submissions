
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        index = 0
        while index < len(nums):
            if index > 0 and nums[index] == nums[index-1]:
                index += 1
                continue

            target = 0 - (nums[index])
            l = index + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[l] + nums[r]

                if currSum == target:
                    if currSum + nums[index] == 0:
                        ans.append([nums[index], nums[l], nums[r]])
                        while l < r-1 and nums[l] == nums[l+1]:
                            l += 1
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        l +=1 
                        r -= 1
                        
                elif currSum < target:
                    l += 1
                else: 
                    r -= 1


            index += 1
       
        return ans