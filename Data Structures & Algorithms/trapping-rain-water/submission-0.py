class Solution:
    def trap(self, height: List[int]) -> int:
        prevMax = []
        nextMax = []
        lenH = len(height)

        tempMax = 0
        for i in range(lenH):
            prevMax.append(tempMax)
            tempMax = max(tempMax, height[i])
        
        tempMax = 0
        for i in range(lenH-1, -1, -1):
            nextMax.insert(0,tempMax)
            tempMax = max(tempMax, height[i])

        ans = 0
        for i in range(1, lenH):
            curr = height[i]
            prevM = prevMax[i]
            nextM = nextMax[i]

            if not (curr < prevM and curr < nextM):
                continue
            
            ans += min(prevM, nextM)-curr

        return ans

