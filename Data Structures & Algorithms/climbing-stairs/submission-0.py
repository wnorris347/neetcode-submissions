class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = [0] * n
        self.n = n

        i = 0
        return self.recursiveStairClimb(i)

    def recursiveStairClimb(self, i:int) -> int:
        if i == self.n:
            return 1
        elif i > self.n:
            return 0
        else:
            if self.cache[i] != 0:
                return self.cache[i]
            else:
                self.cache[i] = self.recursiveStairClimb(i+1) + self.recursiveStairClimb(i+2)
                return self.cache[i]