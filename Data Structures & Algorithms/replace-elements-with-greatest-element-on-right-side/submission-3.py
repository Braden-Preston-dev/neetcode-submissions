class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        greatRight = [0] * len(arr)
        maxs = -1

        for i in range(len(arr) - 1, -1, -1):
            greatRight[i] = maxs
            maxs = max(maxs, arr[i])
        
        return greatRight