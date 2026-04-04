class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack_opened = []
        stack_closed = []
        valid = ""

        for index, c in enumerate(s):
            if c == ")":
                if stack_opened:
                    stack_opened.pop()
                else:
                    stack_closed.append(index)
            elif c == "(":
                stack_opened.append(index)

        whole_stack = sorted(stack_closed + stack_opened)
        j = 0
        for i in whole_stack:
             s = s[:i-j] + s[i-j+1:]
             j +=1
        return s