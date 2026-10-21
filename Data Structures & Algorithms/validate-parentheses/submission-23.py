class Solution:
    def isValid(self, s: str) -> bool:
        
        # maps 
        openToClose = {'}' : '{', ')' : '(', ']': '['}
        stack = [] 

        for c in s:
            if stack and c in openToClose:
                if stack.pop() != openToClose[c]: return False
            else: stack.append(c)

        return True if not stack else False