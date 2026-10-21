class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> uniqueList;

        for(int n : nums) {
            if(uniqueList.contains(n)) return true;
            uniqueList.insert(n);
        }
        return false;
    }
};