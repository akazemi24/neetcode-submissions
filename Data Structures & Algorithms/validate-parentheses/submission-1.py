class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if len(stack) >= 1 and self.isMatch(stack[-1], bracket):
                stack.pop()
            else: 
                stack.append(bracket)
        if len(stack) == 0:
            return True
        else: 
            return False

    def isMatch(self, a: str, b:str) -> bool:
        if a == '(' and b == ')':
            return True
        elif a == '{' and b == '}':
            return True
        elif a == '[' and b == ']':
            return True
        else: 
            return False