class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int maxCount = 0;

        for(int num: nums) {
            count = num == 1 ? ++count : 0; 
            maxCount = max({count, maxCount});
        }
        return maxCount;
    }
};