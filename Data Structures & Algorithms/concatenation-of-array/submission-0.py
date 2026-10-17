class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < 2:
            for j in range(0, len(nums)):
                ans.append(nums[j])
            i += 1
        return ans