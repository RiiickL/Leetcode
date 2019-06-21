class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        len_d = len(digits)
        
        for k in range(1,len_d+1):
            if digits[-k] == 9:
                digits[-k] = 0
            else:
                digits[-k] = digits[-k]+1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
        
        
        