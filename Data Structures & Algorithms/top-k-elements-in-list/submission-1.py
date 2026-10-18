class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        nums.sort()
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        nums = sorted(freq, key=lambda x: freq[x], reverse=True)
        return nums[:k]
        