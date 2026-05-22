class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_l = 0
        outer_r = len(matrix) - 1
        while outer_l <= outer_r:
            #the list of arrays
            outer_m = outer_l + (outer_r - outer_l) // 2
            if matrix[outer_m][0] > target:
                outer_r = outer_m - 1
            elif matrix[outer_m][0] < target:
                outer_l = outer_m + 1
            else:
                return True

            #within the arrays
            l = 0 
            r = len(matrix[outer_m]) - 1
            while l <= r:
                m = l + (r-l) // 2
                if matrix[outer_m][m] > target:
                    r = m - 1
                elif matrix[outer_m][m] < target:
                    l = m + 1
                else:
                    return True

        return False
            
            



    