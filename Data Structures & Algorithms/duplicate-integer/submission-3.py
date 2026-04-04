class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            else:
                hashmap[n] = n
        return False