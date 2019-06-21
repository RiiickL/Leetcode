class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows_num = len(matrix)
        if rows_num==0:
            return False
        cols_num = len(matrix[0])
        if cols_num==0:
            return False
        
        # Find the ID whose value is smaller than target and bigger than next row's
        rows_id = rows_num//2
        rows_len = rows_id//2
        rows_flag = 3
        
        if(matrix[rows_num-1][cols_num-1]<target):
            return False
        if(matrix[0][0]>target):
            return False
        if(matrix[rows_num-1][0]<target):
            rows_id = rows_num-1
        else:
            if rows_len==0:
                rows_len=1
                rows_flag = rows_flag-1
            while(rows_len!=0):
                if(matrix[rows_id][0]==target):
                    return True
                elif(matrix[rows_id][0]<target):
                    rows_id = rows_id+rows_len
                else:
                    rows_id = rows_id-rows_len
                rows_len = rows_len//2
                if((rows_len==0)and(rows_flag!=0)):
                    rows_len = 1
                    rows_flag = rows_flag-1
            if(matrix[rows_id][0]>target):
                rows_id = rows_id-1
            
        # Find the ID 
        cols_id = cols_num//2
        cols_len = cols_id//2
        cols_flag = 3
        if cols_len==0:
            cols_len=1
            cols_flag = cols_flag-1
        while(cols_len!=0):
            if((cols_id<0)or(cols_id==cols_num)):
                return False
            if(matrix[rows_id][cols_id]==target):
                return True
            elif(matrix[rows_id][cols_id]<target):
                cols_id = cols_id+cols_len
            else:
                cols_id = cols_id-cols_len
            cols_len = cols_len//2
            if((cols_len==0)and(cols_flag!=0)):
                cols_len = 1
                cols_flag = cols_flag-1
        return False
        