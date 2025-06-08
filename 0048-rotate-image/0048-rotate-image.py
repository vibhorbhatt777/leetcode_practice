class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #now first we calculate transpose of the matix
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i,len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i] , matrix[i][j]

        
        def reverse_row(matrix):
            for r in range(0,len(matrix)):
                left , right = 0,  len(matrix)-1
                while left < right:
                    matrix[r][left], matrix[r][right] = matrix[r][right] , matrix[r][left]
                    left+=1
                    right-=1
        
        transpose(matrix)
        reverse_row(matrix)



        