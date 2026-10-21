class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        output = 0
        sums = 0
        mapped = {0: 1}

        for i in range(len(nums)):
            sums += nums[i]
            need = sums - k
            output += mapped.get(need, 0)
            mapped[sums] = mapped.get(sums, 0) + 1

        return output