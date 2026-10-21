class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int left, right = 0;
        int len = arr.size();
        vector<int> ans(len);
        int rightMax = -1;
        
        for(int i = len - 1; i >= 0; i--) {
            ans[i] = rightMax;
            rightMax = max({arr[i], rightMax});
        }
            
        return ans;
    }
};