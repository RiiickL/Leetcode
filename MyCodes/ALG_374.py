# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = n//2
        guess_num = d
        while True:
            d = d//2
            if d==0:
                d = 1
            res = guess(guess_num)
            if res==0:
                return guess_num
            else:
                guess_num = guess_num+res*d
        
        
        
        
        
        
        
        