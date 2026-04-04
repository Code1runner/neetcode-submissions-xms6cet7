class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "}":"{", "]": "["}
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() == hashmap[char]:
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
                    
            