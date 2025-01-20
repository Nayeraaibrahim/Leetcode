class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        m = len(mat)  
        n = len(mat[0])  
        value_to_position = {}
        for row in range(m):
            for col in range(n):
                value_to_position[mat[row][col]] = (row, col)

        row_count = [0] * m  
        col_count = [0] * n  
        for i in range(len(arr)):
            value = arr[i]
            if value in value_to_position:
                row, col = value_to_position[value]
                row_count[row] += 1
                col_count[col] += 1
                if row_count[row] == n or col_count[col] == m:
                    return i  
        return -1





            

        