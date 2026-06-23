class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1 for x in nums]
        for i in range(len(nums)):
            for j in range(i):
                prods[i] *= nums[j]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prods[i] *= nums[j]
        return prods