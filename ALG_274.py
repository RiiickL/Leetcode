#   Method 1: statistic & calculate
        
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        length = len(citations)
        counts = [0 for x in range(length)]
		
        # statistic:
        for cit in citations:
            if cit<length:
                counts[cit] = counts[cit]+1
        
        # calculate:
        sumnum = length #the sum number of which over [citnum] in all papers
        for i in range(length):
            sumnum = sumnum-counts[i]
            citnum = i+1
            
            if sumnum<citnum:
                return i
            elif sumnum==citnum:
                return citnum
            
        return length
