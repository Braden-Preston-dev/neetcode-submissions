class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> twoElement;

        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.count(complement)) {
                twoElement.push_back(map.at(complement));
                twoElement.push_back(i);

                return twoElement;
            }
            else map.insert({nums[i], i});
        }
        return twoElement;
    }
};
