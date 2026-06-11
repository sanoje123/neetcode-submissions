class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairOfP = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack and c == pairOfP[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False

        