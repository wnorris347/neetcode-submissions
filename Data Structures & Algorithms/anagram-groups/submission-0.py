class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            seen = [0 for x in range(26)]
            for char in s:
                seen[ord(char)-97] += 1
            res[tuple(seen)].append(s)
        return list(res.values())