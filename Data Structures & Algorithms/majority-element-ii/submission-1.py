class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        majority = len(nums) // 3
        res = set()
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > majority:
                res.add(num)
        return list(res)