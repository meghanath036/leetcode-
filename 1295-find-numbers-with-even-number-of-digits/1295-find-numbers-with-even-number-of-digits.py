class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for val in nums:
            c=0
            while(val>0):
                val=val//10
                c+=1
            if(c%2==0):
                count+=1
        return count
        