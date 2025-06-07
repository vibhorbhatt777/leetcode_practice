class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        col = len(matrix[0])

        result = [[0]*rows for _ in range(col)]

        for i in range(0,rows):
            for j in range(0,col):
                result[j][i] = matrix[i][j]
            print()
        
        return result
        