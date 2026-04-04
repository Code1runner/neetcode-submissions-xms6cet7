class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_map = {}
        for c in magazine:
            char_map[c] = char_map.get(c, 0) + 1

        for c in ransomNote:
            if c in char_map and char_map[c] > 0:
                char_map[c] -= 1
            else:
                return False
        return True