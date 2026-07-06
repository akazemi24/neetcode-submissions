class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        maxcount = 1
        if not nums: 
            return 0
        for i in range(len(nums) - 1): 
            if nums[i+1] - nums[i] == 1:
                count += 1
            elif nums[i+1] - nums[i] == 0:
                continue
            else: 
                if count > maxcount: 
                    maxcount = count
                count = 1
            if count > maxcount: 
                    maxcount = count
        return maxcount

            