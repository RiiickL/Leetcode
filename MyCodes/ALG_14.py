class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_res = ''
        if strs != []:
            for k0 in range(len(strs[0])):
                for k1 in range(1,len(strs)):
                    if not (len(strs[k1])>k0 and strs[k1][k0]==strs[0][k0]):
                        return str_res
                str_res = str_res+strs[0][k0]
        return str_res
            
            
