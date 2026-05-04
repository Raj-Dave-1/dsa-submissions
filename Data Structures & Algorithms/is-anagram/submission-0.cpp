// Dada Ki Jay Ho

class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> freqS(26, 0), freqT(26, 0);
        for(char ch: s)
            freqS[ch-'a']++;
        for(char ch: t)
            freqT[ch-'a']++;
        
        return freqS == freqT;
    }
};
