from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.sort() # nums = sorted(nums)
        freq_dict = defaultdict(int)

        for num in nums: 
            freq_dict[num] += 1
        
        items = freq_dict.items()
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        keys = [val[0] for val in sorted_items]

        return keys[:k]
