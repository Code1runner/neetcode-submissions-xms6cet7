class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            match_s = [0] * 26
            for z in s:
                match_s[ord(z) - ord('a')] += 1
            res[tuple(match_s)].append(s)
        return list(res.values())