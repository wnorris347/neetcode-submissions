class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e = 0, len(matrix)*len(matrix[0])-1
        while s <= e:
            mid = (s+e)//2
            if matrix[mid//len(matrix[0])][mid%len(matrix[0])] > target:
                e = mid - 1
            elif matrix[mid//len(matrix[0])][mid%len(matrix[0])] < target:
                s = mid + 1
            else:
                return True
        return False