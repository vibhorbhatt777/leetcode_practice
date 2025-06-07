class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix) 
        c = len(matrix[0])

        row_track = [0 for _ in range(r)]
        col_track = [0 for _ in range(c)]

        # First pass: identify which rows and columns contain zeros
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1  # CRITICAL: Must be col_track[j], not col_track
        
        # Second pass: set zeros based on tracked rows and columns
        for i in range(0, r):
            for j in range(0, c):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0