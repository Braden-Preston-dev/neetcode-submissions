class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        unordered_map<char, char> map{
            {'}','{'},
            {']','['}, 
            {')', '('}
        };

        for(char c : s) {
            if (map.count(c)) {
                if(!stack.empty() && stack.back() == map[c]) {
                    stack.pop_back();
                }
                else return false;
            }
            else stack.push_back(c);
        }
        return stack.empty();   
    }
};
