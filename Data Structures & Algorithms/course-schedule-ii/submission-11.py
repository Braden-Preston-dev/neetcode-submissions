class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        path = set()
        visit = set()

        premap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in path: return False
            if crs in visit:
                return True

            path.add(crs)
            for p in premap[crs]:
                if not dfs(p): return False
            visit.add(crs)
            path.remove(crs)
            res.append(crs) 
            return True

        for c in range(numCourses):
            if not dfs(c): return []

        return res