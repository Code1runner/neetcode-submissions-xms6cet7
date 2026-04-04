class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_len = len(cardPoints) - k
        max_score = 0
        total = sum(cardPoints)
        i=0
        while i + window_len <= len(cardPoints):
            score = total - sum(cardPoints[i:i+window_len])
            max_score = max(max_score,score)
            i += 1
        return max_score
