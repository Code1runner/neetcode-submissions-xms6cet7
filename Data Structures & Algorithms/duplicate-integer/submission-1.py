class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))
        if len(nums) != len(set(nums)):
            return True
        return False