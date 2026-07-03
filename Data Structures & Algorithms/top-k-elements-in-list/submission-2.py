class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map of frequencies
        count = {}
        # for each number, increment the frequency accordingly
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        # make an array of [frequency, number]
        arr = []
        for num, cnt in count.items():
             arr.append([cnt, num])
        # sort the array in acsending order based on frequency
        arr.sort()

        # get the top k elements of the array
        res = []
        while len(res) < k: 
            res.append(arr.pop()[1])
        return res
        