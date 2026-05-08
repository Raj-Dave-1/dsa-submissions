class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_left_to_right = []
        for x in nums:
            product *= x
            product_left_to_right.append(product)
        
        product = 1
        product_right_to_left = []
        for x in nums[::-1]:
            product *= x
            product_right_to_left.insert(0, product)
        
        print(product_left_to_right)
        print(product_right_to_left)

        ans = []
        for x in range(len(nums)):
            if x == 0:
                ans.append(product_right_to_left[x+1])
            elif x == len(nums)-1: 
                ans.append(product_left_to_right[x-1])
            else:
                ans.append(product_left_to_right[x-1] * product_right_to_left[x+1])

        return ans