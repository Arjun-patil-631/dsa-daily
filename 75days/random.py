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
        