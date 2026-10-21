class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (const string& s : strs) {
            // Build frequency key
            int count[26] = {0};
            for (char c : s) {
                count[c - 'a']++;
            }

            // Serialize count into a string key
            string key;
            for (int i = 0; i < 26; i++) {
                key += '#';
                key += to_string(count[i]);
            }

            groups[key].push_back(s);
        }

        // Collect result
        vector<vector<string>> result;
        for (auto& [_, group] : groups) {
            result.push_back(move(group));
        }

        return result;
    }
};