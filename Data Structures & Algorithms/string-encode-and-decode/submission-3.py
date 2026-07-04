class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs: 
            length = len(string)
            encoded += str(length) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr = 0
        while curr < len(s):
            temp = curr
            while s[temp] != '#':
                temp += 1
            length = int(s[curr: temp])
            curr = temp + 1
            temp = curr + length
            decoded.append(s[curr:temp])
            curr = temp
        return decoded
