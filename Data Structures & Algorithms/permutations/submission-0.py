class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        self.rec(nums, res, idx)
        return res
    
    def rec(self, nums: List[int], res: List[List[int]], idx: int) -> None:
        if idx == len(nums):
            res.append(nums[:])
            return
        
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]

            self.rec(nums, res, idx +1)

            nums[i], nums[idx] = nums[idx], nums[i]