class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        str_ret = '1'
        
        for k in range(n-1):
            count = 0
            char_last = str_ret[0]
            str_tmp = ''
            for char_tmp in str_ret:
                
                if char_tmp == char_last:
                    count = count+1
                else:
                    str_tmp = str_tmp+'%d'%count+char_last
                    char_last = char_tmp
                    count = 1
            str_ret = str_tmp+'%d'%count+char_last
        
        return str_ret
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        