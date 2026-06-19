class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0;
        current_ones = 0;
        for num in nums:
            if num == 1:
                current_ones += 1
                if current_ones > max_consecutive:
                    max_consecutive = current_ones
            else:
                current_ones = 0
        return max_consecutive
        