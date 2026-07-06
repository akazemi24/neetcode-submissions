class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = [0] * len(nums)
        zcount = 0
        for num in nums: 
            if num == 0:
                zcount += 1
            else: 
                product *= num
        if zcount >= 2: 
            return output
        for i, c in enumerate(nums):
            if zcount == 1: 
                output[i] = 0 if c else product
            else: 
                output[i] = product // c
        return output        