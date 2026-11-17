class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left=[0]*len(nums)
        pre=1
        for i in range(0,len(nums)):
            left[i]=pre
            pre*=nums[i]
        right=[0]*len(nums)
        suf=1
        for i in range(len(nums)-1,-1,-1):
            right[i]=suf
            suf*=nums[i]
        result=[0]*len(nums)
        for i in range(0,len(nums)):
            result[i]=left[i]*right[i]
        return result
        
        