#include <iostream>
#include <map>
#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        std::map<char, int> charCountS;
        std::map<char, int> charCountT;

        for (auto const &ch : s) {
            if (charCountS.find(ch) != charCountS.end()) {
                charCountS[ch]++;
            } else {
                charCountS[ch] = 1;
            }
        }

        for (auto const &ch : t) {
            if (charCountT.find(ch) != charCountT.end()) {
                charCountT[ch]++;
            } else {
                charCountT[ch] = 1;
            }
        }

        return charCountS == charCountT;
    }
};
