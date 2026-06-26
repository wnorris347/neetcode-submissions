class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] == -(nums[j]+nums[k]):
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    k -= 1
                    while nums[k] == nums[k+1] and k > j:
                        k -= 1
                elif nums[i] > -(nums[j]+nums[k]):
                    k -= 1
                elif nums[i] < -(nums[j]+nums[k]):
                    j += 1
        return res

