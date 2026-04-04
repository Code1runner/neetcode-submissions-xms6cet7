class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = [0,0,0]
        for i in range(len(nums)):
            l[nums[i]] += 1
        
        index = 0
        for i in range(len(l)):
            for j in range(l[i]):
                nums[index] = i
                index += 1