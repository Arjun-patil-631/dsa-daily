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
#now lets go into depth
class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=sum(nums)

        return expected_sum-actual_sum

#first bad version:

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low=1
        high=n
        result=-1
        while low<=high:
            mid=low+(high-low)//2
            if isBadVersion(mid):
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result
