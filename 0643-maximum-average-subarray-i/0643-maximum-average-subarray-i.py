class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=0
        max1=0
        for i in range(k): #
            w+=nums[i]  #1,12,-5-6=2
        sm=w #4
        for i in range(k,len(nums)): #i=6 6<6
            w=w-nums[i-k]+nums[i] # w=2-nums[1]+nums[5] 51-12+3=42
            sm=max(w,sm) #51,4-->51
        return sm/k #51/5->12.75
        
        