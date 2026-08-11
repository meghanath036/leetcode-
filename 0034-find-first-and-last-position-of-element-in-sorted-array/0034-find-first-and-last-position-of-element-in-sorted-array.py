class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        lval=-1
        fval=-1
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                lval=mid
                left=mid+1
            elif(nums[mid]<target):
                left=mid+1
            elif(nums[mid]>target):
                right=mid-1
            else:
                lval=-1
        left1=0
        right1=len(nums)-1
        while(left1<=right1):
            mid=(left1+right1)//2
            if(nums[mid]==target):
                fval=mid
                right1=mid-1
            elif(nums[mid]<target):
                left1=mid+1
            elif(nums[mid]>target):
                right1=mid-1
            else:
                fval=-1
        l.append(fval)
        l.append(lval)
        return l
        

            
            
        