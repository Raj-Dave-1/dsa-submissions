from collections import defaultdict

class Solution:

    def findFreqList(self, s: str) -> List[int]:
        freq = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] += 1
        return freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: defaultdict[str, List[str]] = defaultdict(list)

        for s in strs:
            freqArray = self.findFreqList(s)
            strRepresentation = ",".join(map(str, freqArray))
            d[strRepresentation].append(s) 
        
        result = list(d.values())

        return result 
