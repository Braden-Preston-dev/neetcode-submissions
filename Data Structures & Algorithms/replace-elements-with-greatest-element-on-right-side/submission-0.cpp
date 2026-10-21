class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int left, right = 0;
        
        for(int i = 0; i < arr.size(); i++) {
            left = i;

            if(right == left){
                right++;
                int j = right;
                while(j < arr.size()){
                    j++;
                    if(arr[j] > arr[right]) right = j;
                }
            }

            arr[left] = arr[right];
        }
        arr[arr.size() - 1 ] = -1;
        return arr;
    }
};