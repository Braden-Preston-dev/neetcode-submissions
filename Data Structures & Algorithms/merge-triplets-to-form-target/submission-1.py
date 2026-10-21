class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        check = [False] * 3

        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue

            if i == target[0]:
                check[0] = True
            if j == target[1]:
                check[1] = True
            if k == target[2]:
                check[2] = True

        return all(check)