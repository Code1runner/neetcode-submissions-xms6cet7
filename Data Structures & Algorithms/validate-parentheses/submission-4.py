class Solution:
    def isValid(self, s: str) -> bool:
        h_map = {")":"(","]":"[","}":"{" }
        stack = []
        if len(s) == 0:
            return True

        for c in s:
            if c in h_map.keys():
                if stack and stack.pop() == h_map[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False