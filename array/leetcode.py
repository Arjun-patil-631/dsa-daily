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

    
#08-7-2026
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
#2nd example of kadane's algorithm:
#correct time to buy and sell stock to maximize profit
class Solution(object):
    def maxProfit(self, prices):
        profit, min_price= 0, prices[0]
        for price in prices:
            if price<min_price:
                min_price=price
            if price-min_price>profit:
                profit=price-min_price
        return profit
        
#09-05-2026
#find the minimum in a rotated sorted array
class Solution(object):
    def findMin(self, nums):
        low, high=0, len(nums)-1
        while low<high:
            mid=(high+low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else: 
                high=mid
        return nums[low]
#or simply return min(nums) but that would be O(n) time complexity, the above solution is O(log n) time complexity

#finding peak element in an array
class Solution(object):
    def findPeakElement(self, nums):
        low, high=0, len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:
                high=mid
            else:
                low=mid+1
        return low      
#or simply return max(nums) but that would be O(n) time complexity, the above solution is O(log n) time complexity

#11-7-2026
#search in a 2D matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=rows*cols-1

        while left<=right:
            mid=(left+right)//2
            r=mid//cols
            c=mid%cols
            value=matrix[r][c]
            if value==target:
                return True
            elif value<target:
                left=mid+1
            else:
                right=mid-1
        return False
    
#rotate a 2D matrix by 90 degrees clockwise
class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
    
#12-05-2026
#rearrange array such that negatives come after positives
class Solution(object):
    def rearrangeArray(self, nums):
        ans=[0]*len(nums)

        pos_ind=0
        neg_ind=1
        for num in nums:
            if num>0:
                ans[pos_ind]=num
                pos_ind+=2
                
            else: 
                ans[neg_ind]=num
                neg_ind+=2
            
        return ans

#greatest permutation of an array
class Solution(object):
    def nextPermutation(self, nums):
        index=-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index== -1:
            nums.reverse()
            return
        for i in range(len(nums)-1,index,-1):
            if nums[i]>nums[index]:
                nums[i], nums[index]=nums[index], nums[i]
                break
        nums[index+1:]=reversed(nums[index+1:])

#13-05-2026
#find all unique triplets in the array which gives the sum of zero
#3sum problem
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                ans=nums[i]+nums[j]+nums[k]
                if ans==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif ans>0:
                    k-=1
                else:
                    j+=1
        return res
    
#14-05-2026
#best time to buy and sell stock to maximize profit
class Solution(object):
    def maxProfit(self, prices):
        profit, min_price= 0, prices[0]
        for price in prices:
            if price<min_price:
                min_price=price
            if price-min_price>profit:
                profit=price-min_price
        return profit
        
#median of two sorted arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num=sorted(nums1+nums2)
        l=len(num)
        if l%2!=0:
            return float(num[l//2])
        else:
            return float(num[l/2]+num[l/2-1])/2

#if array is sorted then 2 sum
class Solution(object):
    def twoSum(self, numbers, target):
        i,j=0,len(numbers)-1
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum==target:
                return [i+1,j+1]
            elif sum>target:
                j-=1
            else:
                i+=1
    
#21-05-2026
#reverse integer
class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        rev=0
        while x!=0:
            d=x%10
            rev=rev*10 + d
            x=x//10
        rev=sign*rev
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev

#24-06-2026
#cycle linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

#26-06-2026
#plus 1
class Solution(object):
    def plusOne(self, digits):
        num=0
        for d in digits:
            num=num*10+d
        num+=1
        return [int(ch) for ch in str(num)]
        
#28-06-2026
#daily question
#maximum element after decreasing and rearranging array
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr[0]=1
        for i in range(1, len(arr)):
            arr[i]=min(arr[i], arr[i-1]+1)
        return arr[-1]
            
#daily question
#29-06-2026
#no of strings that appers as substring in a given string
class Solution(object):
    def numOfStrings(self, patterns, word):
        ans=0
        for pattern in patterns:
            if pattern in word:
                ans+=1
        return ans

