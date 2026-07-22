class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combos = {")": "(",
                "}": "{",
                "]": "["}

        for char in s:
            if char in combos:
                if stack and stack[-1] == combos[char]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(char)
        
        return True if not stack else False