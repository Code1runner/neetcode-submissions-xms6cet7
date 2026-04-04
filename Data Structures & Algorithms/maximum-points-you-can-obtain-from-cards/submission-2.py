class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        r = len(cardPoints) - k
        max_score = total = sum(cardPoints[r:])
        l=0
        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            max_score = max(max_score,total)
            l+=1
            r+=1
        return max_score
