class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        res, cur, visit = [], set(), set()
        premap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        def dfs(c):
            if c in cur: return False
            if c in visit: return True

            cur.add(c)
            
            for pre in premap[c]:
                if not dfs(pre): 
                    return False
                
            
            visit.add(c)
            res.append(c)
            cur.remove(c)
            
            return True


        for c in range(numCourses):
            if not dfs(c): 
                return []
        
        return res