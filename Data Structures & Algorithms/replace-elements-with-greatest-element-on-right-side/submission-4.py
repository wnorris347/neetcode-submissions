class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        pointer = len(arr) - 1
        greatest = -1
        while pointer >= 0:
            temp = arr[pointer]
            arr[pointer] = greatest
            if temp > greatest:
                greatest = temp
            pointer -= 1
        return arr