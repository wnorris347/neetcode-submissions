class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for char in s:
            freq1[char] += 1
        for char in t:
            freq2[char] += 1
        if not len(freq1) == len(freq2):
            return False
        for key, value in freq1.items():
            if not freq2[key] == value:
                return False
        return True