class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_map = {}
        for z in t:
            count_map[z] = count_map.get(z, 0) + 1
        print(count_map)
        for c in s:
            if c in count_map and count_map.get(c) > 0:
                count_map[c] -= 1
            else:
                return False
        return True