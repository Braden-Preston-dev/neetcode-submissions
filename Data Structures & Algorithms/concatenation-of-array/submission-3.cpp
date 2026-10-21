class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans(2 * nums.size());

        for(auto it = nums.begin(); it != nums.end(); it++) {
            int index = it - nums.begin();
            ans[index] = nums[index];
            ans[index + nums.size()] = nums[index];
        }

        return ans;
    }
};