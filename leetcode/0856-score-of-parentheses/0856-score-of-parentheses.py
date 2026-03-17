class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                score_to_add = max(2 * v, 1)
                stack[-1] += score_to_add
                
        return stack[0]
