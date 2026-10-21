class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sCount;
        unordered_map<char, int> tCount;
        
        if(s.length() != t.length()) return false;

        for (int i = 0; i < s.length(); i++) {
            sCount[s[i]]++;
            tCount[t[i]]++;
        }

        return sCount == tCount;
    }
};
