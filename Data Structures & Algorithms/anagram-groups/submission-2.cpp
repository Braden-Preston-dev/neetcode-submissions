class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> groups;
        multimap<vector<int>, string> stringVal;

        for(string& s : strs) {
            vector<int> count(26, 0);

            for(char& c : s){
                count[c - 'a']++;
            }

            stringVal.insert({count, s});
        }

        vector<string> subList;
        for(auto it = stringVal.begin(); it != stringVal.end();) {
            auto range = stringVal.equal_range(it->first);
            for(auto i = range.first; i != range.second; i++) {
                subList.push_back(i->second);
            }
            groups.push_back(subList);
            subList.clear();
            it = stringVal.erase(range.first, range.second);
        }
        return groups;
    }
};
