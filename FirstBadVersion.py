class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=1,n
        
        while (left < right):
            midpoint = (left+right)//2
            
            if isBadVersion(midpoint):
                right = midpoint
        
            else:
                left = midpoint+1
        return left   
