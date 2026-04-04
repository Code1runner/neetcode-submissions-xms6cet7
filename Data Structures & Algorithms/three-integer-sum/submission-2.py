class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    hashmap[(i,j)] = nums[i] + nums[j]
        
        for i in range(len(nums)):
             for key,value in hashmap.items():
                if value+nums[i] == 0 and i not in key:
                    sorted_res = sorted([nums[i], nums[key[0]], nums[key[1]]])
                    if sorted_res not in res:
                        res.append(sorted_res)
        return res