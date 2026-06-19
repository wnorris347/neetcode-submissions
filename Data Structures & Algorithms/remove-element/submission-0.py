class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        instances = 0
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = 51
                instances += 1
        k = len(nums) - instances
        nums.sort()
        return k
        