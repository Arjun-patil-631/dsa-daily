#missing numbers
#classical binary solution:
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==mid:
                low=mid+1
            else:
                high=mid-1
        return low
