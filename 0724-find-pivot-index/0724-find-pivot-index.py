class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        add=sum(nums)
        for i in range(len(nums)):
            if(left==(add-left-nums[i])) : 
                return i
            else:
                left+=nums[i]  
        return -1       
        