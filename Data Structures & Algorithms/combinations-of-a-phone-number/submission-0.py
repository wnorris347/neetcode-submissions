class Solution:


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        idx = 0
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.rec(digits, res, idx, d, "")
        return res
    
    def rec(self, digits: str, res: List[str], idx: int, d, perm: str) -> None:
        if len(perm) == len(digits):
            res.append(perm)
            return
        
        for i in range(len(d[digits[idx]])):
            self.rec(digits, res, idx + 1, d, perm + d[digits[idx]][i])

        
        