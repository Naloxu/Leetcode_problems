#include <iostream>
#include <map>
#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        std::map<char, int> charCount;

        if (s.size() != t.size()) { return false; }

        for (auto const &ch : s) {
            charCount[ch]++;
        }

        for (auto const &ch : t) {
            charCount[ch]--;
            if (charCount[ch] < 0) {
                return false;
            }
            
        }
        return true;
    }
};