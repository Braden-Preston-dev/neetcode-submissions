class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        sol = []

        for i, num in enumerate(nums):
            complement = target - num

            if lookup.get(complement) is not None:
                sol.append(lookup[complement])
                sol.append(i)
                return sol
                
            lookup[num] = i
        return sol 