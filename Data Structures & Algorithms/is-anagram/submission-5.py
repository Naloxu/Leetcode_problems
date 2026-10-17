class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_frequency = {}
        t_letter_frequency = {}
        for c in s:
            s_letter_frequency[c] = s_letter_frequency.get(c, 0) + 1
        for c in t:
            t_letter_frequency[c] = t_letter_frequency.get(c, 0) + 1
        if s_letter_frequency == t_letter_frequency:
            return True
        return False