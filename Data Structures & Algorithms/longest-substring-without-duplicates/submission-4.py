class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        dups = set()

        for r in range(len(s)):

            while s[r] in dups:
                dups.remove(s[l])
                l+= 1

            dups.add(s[r])
            max_len = max(max_len, r-l+1)

        return max_len

            

