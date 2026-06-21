class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) > 0:
                if char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return len(stack) == 0
        