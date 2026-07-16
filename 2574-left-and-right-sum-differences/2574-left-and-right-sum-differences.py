class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        add=0
        l=[]
        left=0
        for i in range(len(nums)):
           add+=nums[i]
        for i in range(len(nums)):
            res=abs(left-(add-nums[i]-left))
            l.append(res)
            left+=nums[i]
        return l
