# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        return bin(x^y).count('1')
    
    
    
sol = Solution()
z = sol.hammingDistance(2,11)
print(z)




