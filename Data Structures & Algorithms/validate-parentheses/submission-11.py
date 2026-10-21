class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {')' : '(',
        '}' : '{',
        ']' : '['}

        for c in s:
            if stack and c in pairs:
                if stack.pop() != pairs[c]:
                    return False
            elif c == '(' or '{' or '[':
                stack.append(c)
            else: return False
        if stack: return False
        else: return True