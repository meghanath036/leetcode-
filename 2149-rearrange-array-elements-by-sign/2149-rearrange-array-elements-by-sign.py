class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in range(0,len(nums)):
            if(nums[i]>=0):
                p.append(nums[i])
            else:
                n.append(nums[i])
        k=0
        for i in range(0,len(n)):
            nums[k]=p[i]
            k+=1
            nums[k]=n[i]
            k+=1
        return nums
        