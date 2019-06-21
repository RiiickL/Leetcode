class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for m in range(n//2):
            for k in range(n-m*2-1):
                matrix[m][m+k],matrix[m+k][n-m-1],matrix[n-m-1][n-1-m-k],matrix[n-1-m-k][m] = matrix[n-1-m-k][m],matrix[m][m+k],matrix[m+k][n-m-1],matrix[n-m-1][n-1-m-k]