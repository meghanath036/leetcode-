class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[0]*len(nums)
        pref=1
        for i in range(0,len(nums)):
            left[i]=pref
            pref*=nums[i]
        suff=1
        for i in range(len(nums)-1,-1,-1):
            left[i]=suff*left[i]
            suff*=nums[i]
        return left

        