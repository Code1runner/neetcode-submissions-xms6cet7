class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        match = {}
        for n in nums:
            match[n] = match.get(n,0) + 1
        match = dict(sorted(match.items(), key=lambda match: match[1], reverse=True))
        return list(match.keys())[:k]