class Solution:
    def search_Matrix(self, matrix, target):
        check_row = 0
        end_row = len(matrix) - 1
        while check_row <= end_row:
            start = 0
            end = len(matrix[0]) - 1
            while start <= end:
                mid = int((start + end)/2)
                if matrix[check_row][mid] == target:
                    return True
                elif matrix[check_row][mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            check_row += 1
        return False


sol = Solution()
print(sol.search_Matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))