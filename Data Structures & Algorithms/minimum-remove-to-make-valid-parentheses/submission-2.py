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

        whole_stack = stack_closed + stack_opened
        s = "".join([l for index,l in enumerate(s) if index not in whole_stack])
        return s