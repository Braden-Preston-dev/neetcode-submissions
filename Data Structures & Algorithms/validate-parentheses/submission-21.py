class Solution:
    def isValid(self, s: str) -> bool:
        
        close = { '}' : '{',
        ']' : '[',
        ')' : '('
        }
        stack = []
        for c in s:
            if c in close:
                if not stack or stack.pop() != close[c]: return False
            else: stack.append(c)
        return True if not stack else False