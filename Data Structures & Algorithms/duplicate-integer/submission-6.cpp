class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> uniqueList;

        for(int n : nums) {
            if(uniqueList.count(n)) return true;
            uniqueList.insert(n);
        }
        return false;
    }
};