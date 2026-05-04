// Dada Ki Jay Ho
#include <map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> freq;
        for(int ele: nums){
            if(freq[ele]) return true;
            freq[ele] = 1;
        }
        return false;
    }
};