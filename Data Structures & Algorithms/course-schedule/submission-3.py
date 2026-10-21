class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap = {i: [] for i in range(numCourses)}
        path = set()

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in path: return False
            if premap[crs] == []: return True

            path.add(crs)
            for p in premap[crs]:
                if not dfs(p): return False
            premap[crs] = []
            path.remove(crs)
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True