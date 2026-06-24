from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1: return False
        queue = deque()
        def compliant(left, right):
            if left == '{' and right == '}': return True
            if left == '(' and right == ')': return True
            if left == '[' and right == ']': return True
            return False
        for char in s:
            if char in ['{', '(', '[']:
                queue.append(char)
            elif not queue or not compliant(queue.pop(), char):
                return False
        return True if not queue else False