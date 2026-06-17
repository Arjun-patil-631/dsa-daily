#TREES
#11-06-2026
#preorder traversal of a binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        arr = []
        def preorder(node):
            if not node:
                return
            arr.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return arr

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result=[]
        def postorder(node):
            if not node:
                return 
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        postorder(root)
        return result

#12-06-2026
#min stack
class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, value):
        self.stack.append(value)
        if not self.minstack:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value, self.minstack[-1]))

    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]

#linked list
#14-06-2026
#rotate list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head
        n=1
        tail=head
        while tail.next:
            tail=tail.next
            n+=1
        k %=n
        if k==0:
            return head
        #make it circular list
        tail.next=head

        steps=n-k-1
        new_tail=head

        for _ in range(steps):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None

        return new_head

#15-06-2026
#linked list
#delete the middle node of a linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        temp=head
        n=0
        while temp:
            n+=1
            temp=temp.next
        
        mid=n//2

        temp=head
        for _ in range(mid-1):
            temp=temp.next

        temp.next=temp.next.next
        return head
#time complexity O(n)
#84 ms

#other approach #use this (preffered) better approach
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
         # If there's only one node
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

        return head
#this method is known as the "tortoise and hare" approach,
# where the slow pointer moves one step at a time and the fast pointer 
#moves two steps at a time. 

#daily challenge
#16-06-2026
#process string with special operations -1
class Solution(object):
    def processStr(self, s):
        result=[]
        for ch in s:
            if ch=="*":
                if result:
                    result.pop()
            elif ch=="#":
                result+=result
            elif ch=="%":
                result=result[::-1]
            elif ch>="a" and ch<="z":
                result.append(ch)
        return "".join(result)

#daily challenge
#17-06-2026
#process string with special operations -2
class Solution(object):
    def processStr(self, s, k):
        length = 0

        # Calculate final length
        for ch in s:
            if ch == '*':
                length = max(0, length - 1)
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
            else:
                length += 1

        if k >= length:
            return '.'

        # Reverse simulation
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch == '*':
                length += 1

            elif ch == '#':
                length //= 2
                if k >= length:
                    k -= length

            elif ch == '%':
                k = length - 1 - k

            else:  # letter
                length -= 1
                if k == length:
                    return ch

        return '.'