class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        indexes = []
        for index, num in enumerate(numbers):
            if target-num in dic:
                indexes = [dic[target-num]+1, index+1]
                break;
            dic[num] = index
        return indexes