class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]:
            return []
        
        rows_num = len(matrix)
        cols_num = len(matrix[0])
        dirc_lim = [0 for x in range(4)]
        dirc_lim[0] = cols_num-1
        dirc_lim[1] = rows_num-1
        dirc_lim[2] = 0
        dirc_lim[3] = 1
        
        pos = [0 for x in range(2)]
        list_ret = [matrix[pos[0]][pos[1]]]
        
        def pos_move(dirc,pos):
            if dirc==0:
                pos[1] = pos[1]+1
                if pos[1]>dirc_lim[0]:
                    pos[1] = pos[1]-1
                    ret_flag = False
                else:
                    ret_flag = True
            elif dirc==1:
                pos[0] = pos[0]+1
                if pos[0]>dirc_lim[1]:
                    pos[0] = pos[0]-1
                    ret_flag = False
                else:
                    ret_flag = True
            elif dirc==2:
                pos[1] = pos[1]-1
                if pos[1]<dirc_lim[2]:
                    pos[1] = pos[1]+1
                    ret_flag = False
                else:
                    ret_flag = True
            else:
                pos[0] = pos[0]-1
                if pos[0]<dirc_lim[3]:
                    pos[0] = pos[0]+1
                    ret_flag = False
                else:
                    ret_flag = True
            
            if ret_flag:
                list_ret.append(matrix[pos[0]][pos[1]])
            return ret_flag
            
        dirc = 0
        while(True):
            if not pos_move(dirc,pos):
                if dirc<2:
                    dirc_lim[dirc] = dirc_lim[dirc]-1
                else:
                    dirc_lim[dirc] = dirc_lim[dirc]+1
                dirc = (dirc+1)%4
                if not pos_move(dirc,pos):
                    break
        
        return list_ret
            
    def test(self):
        
        matrix = [[1],[4],[7]]
        list_ret = self.spiralOrder(matrix)
        
        print(list_ret)