class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=float('-inf')
        sum=0
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            if(sum>max):
                max=sum
            if(sum<0):
                sum=0
        return max
