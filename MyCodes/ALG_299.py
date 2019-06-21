class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = [0 for x in range(10)]
        guess_count = [0 for x in range(10)]
        bulls_count = 0
        cows_count = 0
        for k in range(len(secret)):
            if secret[k]==guess[k]:
                bulls_count=bulls_count+1
            else:
                pos = int(secret[k])
                if guess_count[pos]>0:
                    cows_count = cows_count+1
                    guess_count[pos] = guess_count[pos]-1
                else:
                    secret_count[pos]=secret_count[pos]+1
                pos = int(guess[k])
                if secret_count[pos]>0:
                    cows_count = cows_count+1
                    secret_count[pos] = secret_count[pos]-1
                else:
                    guess_count[pos]=guess_count[pos]+1
        return str(bulls_count)+'A'+str(cows_count)+'B'
    def test(self)
        x = '2213'
        y = '2333'
        z = self.getHint(x,y)
        print(z)
        
        
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counts = [0 for x in range(10)]
        bulls_count = 0
        cows_count = 0
        for k in range(len(secret)):
            if secret[k]==guess[k]:
                bulls_count=bulls_count+1
            else:
                secret_num = int(secret[k])
                guess_num = int(guess[k])
                if counts[secret_num]>0:
                    cows_count = cows_count+1
                counts[secret_num] = counts[secret_num]-1
                if counts[guess_num]<0:
                    cows_count = cows_count+1
                counts[guess_num] = counts[guess_num]+1
        return str(bulls_count)+'A'+str(cows_count)+'B'
        
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_counts = [0 for x in range(10)]
        g_counts = s_counts
        bulls_count = 0
        cows_count = 0
        for k in range(len(secret)):
            secret_num = int(secret[k])
            guess_num = int(guess[k])
            if secret_num==guess_num:
                bulls_count=bulls_count+1
            else:
                s_counts[secret_num] = s_counts[secret_num]+1
                c_counts[guess_num] = c_counts[guess_num]+1
                
                
