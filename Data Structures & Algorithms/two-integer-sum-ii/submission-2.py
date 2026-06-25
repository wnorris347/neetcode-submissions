class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        while left < len(numbers)-1:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif right < len(numbers)-1:
                right += 1
            else:
                left += 1
                right = left + 1