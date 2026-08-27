class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        is_found=False
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1]):
                is_found=True
                break
        return is_found
    

        