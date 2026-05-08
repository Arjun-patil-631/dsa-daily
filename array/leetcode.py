#remove duplicates from sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        seen=set()
        index=0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index]=num
                index+=1
        return index

#find the single number in an array where every element appears twice except for one
class Solution(object):
    def singleNumber(self, nums):
        xor =0
        for num in nums:
            xor=xor^num
        return xor

#majority element in an array
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        el=0
        cnt=0
        for num in nums:
            if cnt==0:
                cnt=1
                el=num
            elif el==num:
                cnt+=1
            else:
                cnt-=1
        cnt1=nums.count(el)
        if cnt1 > (n//2):
            return el
        return -1

#check if array is sorted and rotated
class Solution(object):
    def check(self, nums):
        count=0
        n=len(nums)
        for i in range(0, n):
                if nums[i]>nums[(i+1)% n]:
                    count+=1
        return count<=1
        
#rotate array to right by k steps
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k=k%n
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])

    
#08-7-2025
#kadane's algorithm to find maximum subarray sum
class Solution(object):
    def maxSubArray(self, nums):
        max, sum=nums[0],0
        for num in nums:
            sum+=num
            if sum>max:
                max=sum
            if sum<0:
                sum=0
        return max
        