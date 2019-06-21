class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_x = [('(',1,0)]
        list_ret = []
        while len(list_x):
			x = list_x.pop()
			if x[1]==n:
				x2 = x[2]
				x0 = x[0]
				while x2 != n:
					x0 = x0+')'
					x2 = x2+1
				list_ret.append(x0)
			else:
				x1 = (x[0]+'(', x[1]+1, x[2])
				list_x.insert(0,x1)
				if x[2] != x[1]:
					x2 = (x[0]+')', x[1], x[2]+1)
					list_x.insert(0,x2)
        return list_ret
        