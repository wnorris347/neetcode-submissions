class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+"#"+s
        return result
    def decode(self, s: str) -> List[str]:
        pointer = 0
        result = []
        while pointer < len(s):
            digits = ""
            while not s[pointer] == "#":
                digits += (s[pointer])
                pointer += 1
            pointer += 1
            length = int(digits)
            result.append(s[pointer:pointer+length])
            pointer += length
        return result