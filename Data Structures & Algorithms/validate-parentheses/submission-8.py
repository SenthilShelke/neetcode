class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(stack) > 0:
                    if s[i] == ')' and stack.pop() != '(':
                        return False
                    elif s[i] == ']' and stack.pop() != '[':
                        return False
                    elif s[i] == '}' and stack.pop() != '{':
                        return False
                else:
                    return False
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        else:
            return False



