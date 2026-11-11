class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        odd_freq = -1
        even_freq = -1
        for _, v in freq:
            if v % 2 == 1 and odd_freq == -1:
                odd_freq = v  
            if v % 2 == 0:
                even_freq = v         

        return odd_freq - even_freq   