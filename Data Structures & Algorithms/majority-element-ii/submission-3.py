class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        majority = len(nums) // 3
        res = []
        for num in count:
            if count[num] > majority:
                res.append(num)
        return res