class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = defaultdict(list)

        for i in range(len(nums)):
            duplicates[nums[i]].append(i)
        
        for key in duplicates:
            if len(duplicates[key]) > 1 and abs(duplicates[key].pop() - duplicates[key].pop()) <= k: return True

        return False