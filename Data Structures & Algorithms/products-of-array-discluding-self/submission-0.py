class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_index = []
        for i,n in enumerate(nums):
            if n != 0:
                total *= n
            else:
                total *= 1
                zero_index.append(i)
        if len(zero_index) > 1:
            return [0] * len(nums)
        elif len(zero_index) == 1:
            output = [0] * len(nums)
            output[zero_index[0]] = total
            return output
        else:
            return [total // n for n in nums]