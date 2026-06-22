class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0,0,0]
        for color in nums:
            counts[color] += 1
        
        i = 0
        for x, count in enumerate(counts):
            for j in range(count):
                nums[i] = x
                i += 1
        