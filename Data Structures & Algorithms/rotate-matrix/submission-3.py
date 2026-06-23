class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        n = len(matrix[0])
        j=0
        for i in range (0,n):
            for j in range(i+1,n):
                a = matrix[i][j]
                b = matrix[j][i]
                matrix [i][j]=b
                matrix[j][i] =a
        # return matrix
                
        for i in range(0,n):
            for j in range(0,n//2):
                    a=matrix [i][j]
                    b = matrix[i][n-1-j]
                    matrix [i][j]=b
                    matrix[i][n-j-1] =a
        # return matrix
    



        