class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = 0
        stack = []
        for c in abbr:
            if c.isdigit():
                if num == 0 and int(c) == 0:
                    return False
                num = num*10 + int(c)
            else:
                if num > 0:
                    stack.append(num)
                    num = 0
                stack.append(c)
        if num > 0:
            stack.append(num)
        
        i = 0
        for part in stack:
            if isinstance(part, int):
                i += part
            else:
                if i >= len(word) or word[i] != part:
                    return False
                else:
                    i += 1
        return i == len(word)
        