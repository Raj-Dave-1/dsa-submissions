
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        index = 0
        visited = set()
        while index < len(nums):
            while index < len(nums)-1 and nums[index] in visited:
                index += 1
            visited.add(nums[index])
            target = 0 - (nums[index])
            l = index + 1
            r = len(nums) - 1

            visitedL = set()
            visitedR = set()
            while l < r:
                currSum = nums[l] + nums[r]

                if currSum == target and nums[l] not in visitedL and nums[r] not in visitedR:
                    if currSum + nums[index] == 0:
                        ans.append([nums[index], nums[l], nums[r]])
                        visitedL.add(nums[l])
                        visitedR.add(nums[r])
                        l +=1 
                        r -= 1
                        
                elif currSum < target:
                    l += 1
                else:
                    r -= 1

            index += 1
       
        return ans