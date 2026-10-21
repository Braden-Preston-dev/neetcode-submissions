class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = nums.size();

        for(auto it = nums.begin(); it != nums.end();){
            if(*it == val) {
                nums.erase(it);
                k--;
             }
            else ++it;
        }
        return k;
    }
};