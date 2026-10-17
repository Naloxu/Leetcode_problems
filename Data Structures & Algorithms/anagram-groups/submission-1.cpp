#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;
        for (const string& str : strs) {
            vector<int> charCount(26, 0);
            for (char c : str) {
                charCount[c - 'a']++;
            }
            string key = to_string(charCount[0]);
            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(charCount[i]);
            }
            anagramMap[key].push_back(str);
        }
        vector<vector<string>> result;
        for (const auto& pair : anagramMap) {
            result.push_back(pair.second);
        }
        return result;
    }
};
