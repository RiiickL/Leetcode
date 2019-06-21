class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows_num = len(grid)
        cols_num = len(grid[0])
        
        for k in range(1,rows_num+cols_num-1):
            
            if k<cols_num:
                row_from = 0
            else:
                row_from = k-cols_num+1
            
            tmp_row = row_from
            tmp_col = k-row_from
            while(tmp_col>=0 and tmp_row<rows_num):
                #print(tmp_row,tmp_col,'\n')
                if tmp_row==0:
                    grid[tmp_row][tmp_col] = grid[tmp_row][tmp_col]+grid[tmp_row][tmp_col-1]
                elif tmp_col==0:
                    grid[tmp_row][tmp_col] = grid[tmp_row][tmp_col]+grid[tmp_row-1][tmp_col]
                else:
                    if grid[tmp_row][tmp_col-1]<grid[tmp_row-1][tmp_col]:
                        grid[tmp_row][tmp_col] = grid[tmp_row][tmp_col]+grid[tmp_row][tmp_col-1]
                    else:
                        grid[tmp_row][tmp_col] = grid[tmp_row][tmp_col]+grid[tmp_row-1][tmp_col]
                
                tmp_row = tmp_row+1
                tmp_col = k-tmp_row
                
        return grid[rows_num-1][cols_num-1]
        
    def test(self):
        grid = [[1,2],[1,3]]
        print(self.minPathSum(grid))
        
        
        