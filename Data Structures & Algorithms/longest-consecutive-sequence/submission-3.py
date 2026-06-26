class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)
        longest = 0
        for num in numbers:
            if (num-1) not in numbers:
                i = num
                seq_length = 1
                while i+1 in numbers:
                    i += 1
                    seq_length += 1
                if seq_length > longest:
                    longest = seq_length
        return longest