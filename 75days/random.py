#13-05-2025
#find difference between two arrays
# below is my method 
# efficiency: O(n*m) where n and m are the lengths of the two arrays -638ms
class Solution(object):
    def findDifference(self, nums1, nums2):
        ans1=[]
        ans2=[]
        for num in nums1:
            if num not in nums2:
                if num not in ans1:
                    ans1.append(num)
        for num in nums2:
            if num not in nums1:
                if num not in ans2:
                    ans2.append(num)
        return [ans1,ans2]
#efficient method using sets -7ms!!
class Solution(object):
    def findDifference(self, nums1, nums2):
        fset=set(nums1)
        sset=set(nums2)
        res=[]
        res.append(list(fset-sset))
        res.append(list(sset-fset))
        return res
    
#revering a llinked list iteratively
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse link
            prev = curr             # move prev ahead
            curr = next_node        # move curr ahead

        return prev

#recursive method to reverse a linked list        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # Base case
        if not head or not head.next:
            return head

        # Reverse remaining list
        new_head = self.reverseList(head.next)

        # Reverse current connection
        head.next.next = head
        head.next = None

        return new_head
        
#is valid parentheses
class Solution(object):
    def isValid(self, s):
        oA, oB, oC=0,0,0
        for ch in s:
            if ch=="(":
                oA+=1
            if ch=="{":
                oB+=1
            if ch=="[":
                oC+=1
            elif ch=="]":
                oC-=1
            elif ch==")":
                oA-=1
            elif ch=="}":
                oB-=1
        if oA==0 and oB==0 and oC==0:
            return True
        else:
            return False
#but it will fail for cases like "([)]" where the order of closing brackets is wrong.

#efficient method using stack
class Solution(object):
    def isValid(self, s):
        stack=[]
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack: 
                    return False
                top=stack.pop()
                if ch==")" and top!="(":
                    return False
                if ch=="]" and top!="[":
                    return False
                if ch=="}" and top!="{":
                    return False
        return len(stack)==0

#27-05-2026
#number of speacial characcters II
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low={}
        upp={}

        for i, ch in enumerate(word):
            if ch.islower():
                low[ch]=i
            else:
                lower=ch.lower()
                if lower not in upp:
                    upp[lower]=i
        count=0
        for ch in low:
            if ch in upp:
                if low[ch]<upp[ch]:
                    count+=1
        return count

#longest valid parentheses
class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        ans=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans=max(ans, i-stack[-1])
        return ans

#29-05-2026
#min element after replacing with sum of digits
class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            sum=0
            for n in str(nums[i]):
                sum+=int(n)
            nums[i]=sum
        return min(nums)

#1-6-2026
#69-sqrt without inbuilt functions
class Solution(object):
    def mySqrt(self, x):
        left,right=0,x
        ans=0
        while left<=right:
            mid=(left+right)//2
            if mid*mid<=x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans

#delete a node in a linked list
# Definition for singly-linked list.
# class ListNode(object):   
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

#3-06-2026
#insterction of two linked lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p1,p2=headA, headB
        while p1!=p2:
            p1=p1.next if p1 else headB
            p2=p2.next if p2 else headA
        return p1

#10-06-2026
#number of steps to reduce a number to zero
class Solution(object):
    def numberOfSteps(self, num):
        count=0
        while num!=0:
            if num%2==0:
                num=num/2
            else: 
                num=num-1
            count+=1
        return count

#21-06-2026
#find the min in a rotated sorted array I
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
    

#find the min in a rotated sorted array II
"""in this case we can have duplicates in the array 
   so we will have to check for the case when mid and high are
   same and we will have to reduce the high by 1 in that case """
class Solution(object):
    def findMin(self, nums):
        low, high=0, len(nums)-1
        while low<high:
            mid=(high+low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            elif nums[mid]<nums[high]:
                high=mid
            else:
                high-=1
        return nums[low]
    
#27-06-2026
#climbing stairs
class Solution(object):
    def climbStairs(self, n):
        if n<=2:
            return n
        first=1
        second=2
        for i in range(3,n+1):
            first, second= second, first+second
        return second

#remove element from an array
class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

#2-7-2026
#excel sheet column title

#iterative method( 14 ms  in leetcode)
class Solution(object):
    def convertToTitle(self, columnNumber):
        ans = ""

        while columnNumber:
            columnNumber -= 1
            ans = chr(columnNumber % 26 + ord('A')) + ans
            columnNumber //= 26

        return ans
               
#recursive method( 0 ms  in leetcode)
class Solution(object):
    def convertToTitle(self, columnNumber):
        if columnNumber == 0:
            return ""

        columnNumber -= 1
        return self.convertToTitle(columnNumber // 26) + chr(columnNumber % 26 + ord('A'))  