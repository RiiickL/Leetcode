class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h_nums = len(height)
        max_value = 0
        max_height = 0
        ptr_head = 0
        ptr_tail = h_nums-1
        for width in range(h_nums-1,0,-1):
            if height[ptr_head]<height[ptr_tail]:
                if height[ptr_head]>max_height:
                    max_height = height[ptr_head]
                    max_value = max(max_value,max_height*width)
                ptr_head = ptr_head+1
            else:
                if height[ptr_tail]>max_height:
                    max_height = height[ptr_tail]
                    max_value = max(max_value,max_height*width)
                ptr_tail = ptr_tail-1
        return max_value

        
        
        
        