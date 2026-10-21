class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        path = set()
        premap = {i: [] for i in range(n)}

        for head, nextHead in edges:
            premap[head].append(nextHead) 
            premap[nextHead].append(head)
        
        def dfs(node, parent):
            if node in path: return False
            
            path.add(node)

            for p in premap[node]:
                if p == parent:
                    continue
                if not dfs(p, node):
                    return False

            return True

        return dfs(0, -1) and len(path) == n