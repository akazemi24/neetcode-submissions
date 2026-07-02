class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create hash map
        res = defaultdict(list)
        for s in strs: 
            # create empty array 
            count = [0] * 26
            # for each character in the string
            for c in s: 
                # get alphabet value from 0 to 25
                count[ord(c) - ord('a')] += 1
            # key is the count array
            # value is a list of strings
            res[tuple(count)].append(s)
        return list(res.values())
        