class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first,last=0,len(nums)-1
        
        while first <= last:
            midpoint = first+(last-first)//2
            
            if nums[midpoint]==target:
                return midpoint
        
            elif nums[midpoint]<target:
                first= midpoint+1
            
            else:
                last= midpoint-1
        return -1    
    
