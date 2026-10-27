class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        if freq[0][1] >= len(nums) / 2:
            return freq[0][0]