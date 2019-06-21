class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        
        L = [[1 for x in range(n)] for x in range(n)]
        Pos = [0,0]
        Dirc = 0
        Limt = [n-1, n-1, 0, 1]
        
        def movePos(Pos, Dirc):
            if Dirc == 0:
                if Pos[1]==Limt[0]:
                    return False
                else:
                    Pos[1] = Pos[1]+1
            elif Dirc == 1:
                if Pos[0]==Limt[1]:
                    return False
                else:
                    Pos[0] = Pos[0]+1
            elif Dirc == 2:
                if Pos[1]==Limt[2]:
                    return False
                else:
                    Pos[1] = Pos[1]-1
            else:
                if Pos[0]==Limt[3]:
                    return False
                else:
                    Pos[0] = Pos[0]-1
            return True
        
        for k in range(2,n*n+1):
            if not movePos(Pos, Dirc):
                if Dirc<2:
                    Limt[Dirc] = Limt[Dirc]-1
                else:
                    Limt[Dirc] = Limt[Dirc]+1
                Dirc = (Dirc+1)%4
                movePos(Pos, Dirc)
            L[Pos[0]][Pos[1]] = k
        return L
            
    def test(self):
        print(self.generateMatrix(3))
            
        
        
        
        