class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        min_path = [0 for x in range(len(triangle))]
        min_path[0] = triangle[0][0]
        last_length = 1
        for n_list in triangle[1:]:
            # head
            min_tmp = min_path[0]
            min_path[0] = min_path[0]+n_list[0]
            # body
            for body_id in range(1,last_length):
                min_tmp,min_path[body_id] = min_path[body_id],min(min_tmp,min_path[body_id])+n_list[body_id]
            # tail
            min_path[last_length] = min_tmp+n_list[last_length]
            last_length = last_length+1
        return min(min_path)
            
            
            
            
            
        
        
        
        
        