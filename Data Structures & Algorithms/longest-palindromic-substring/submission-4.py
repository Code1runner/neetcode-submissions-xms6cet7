class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = 0
        pal = ""
        if len(s) == 1:
            return s
        for l in range(len(s)):
            for r in range(l, len(s)+1):
                curr_s = s[l:r]
                if curr_s == curr_s[::-1] and len(curr_s) > len(pal):
                    pal = curr_s
        return pal
            