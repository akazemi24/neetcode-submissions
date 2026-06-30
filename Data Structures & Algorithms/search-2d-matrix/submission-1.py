class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix: 
            if target >= row[0] and target <= row[-1]:
                return self.binarySearch(row, target)
        return False

    def binarySearch(self, row: List[int], target: int) -> bool:
        high = len(row) -1
        low = 0

        while (low <= high):
            mid = (low + (high-low)//2)
            if target > row[mid]:
                low = mid + 1
            elif target < row[mid]:
                high = mid - 1
            else: 
                return True
        return False

        