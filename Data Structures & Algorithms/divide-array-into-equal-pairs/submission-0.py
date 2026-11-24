class Solution:
    def divideArray(self, nums) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
                
        for v in seen.keys():
            if seen[v] % 2 == 0:
                continue
            else:
                return False
        return True
