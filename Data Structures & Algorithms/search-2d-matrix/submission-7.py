class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        row = 0

        while d >= u:
            row = (d + u) // 2
            if target > matrix[row][-1]:
                u = row + 1
            elif target < matrix[row][0]:
                d = row - 1
            else:
                break
        else: return False

        row = (d + u) // 2

        while r >= l:
            m = (r + l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

