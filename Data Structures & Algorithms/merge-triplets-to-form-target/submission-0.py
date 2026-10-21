class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = []
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]: continue
            res.append([i, j, k])
        
        check = [False] * 3
        for i, j, k in res:
            if target[0] == i: check[0] = True
            if target[1] == j: check[1] = True
            if target[2] == k: check[2] = True
        return all(check)