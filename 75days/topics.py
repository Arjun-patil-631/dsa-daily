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

#18-06-2026
#mirror image
class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

#19-06-2026
#container with most water
class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        maxi=0
        while i<j:
            area=min(height[i], height[j])*(j-i)
            maxi=max(maxi, area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxi

#daily problem
#22-06-2026
#max number of ballons
# by using in-built counter function
from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        c=Counter(text)
        return min(
            c['b'],
            c['a'],
            c['l']//2,
            c['o']//2,
            c['n']
        )
#time complexity O(n)  13ms on leetcode

#without using counter function
class Solution(object):
    def maxNumberOfBalloons(self, text):
        b=text.count("b")
        a=text.count("a")
        l=text.count("l")
        o=text.count("o")
        n=text.count("n")
        count=0
        while b>=1 and a>=1 and l>=2 and o>=2 and n>=1:
            b-=1
            a-=1
            l-=2
            o-=2
            n-=1
            count+=1
        return count
#time complexity O(n)  0 ms on leetcode

#23-06-2026
#binary tree path
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        ans=[]

        def dfs(node, path):
            if not node:
                return 
            path+=str(node.val)
            if not node.right and not node.left:
                ans.append(path)
                return
            path+="->"
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, "")
        return ans

#30-06-2026
#happy number
#a number is happy if it leads to 1 after a sequence of steps
#where each step involves replacing the number by the sum of squares of its digits
class Solution(object):
    def getNext(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n):
        slow = n
        fast = self.getNext(n)

        while fast != 1 and slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return fast == 1

#3-07-2026
#count and say
class Solution(object):
    def countAndSay(self, n):
        s="1"
        for _ in range(n-1):
            res=[]
            count=1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(s[i - 1])
                    count = 1

            res.append(str(count))
            res.append(s[-1])
            s = "".join(res)

        return s

#daily
#6-07-2026
#remove covered intervals
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end

        return count

#daily 
#07-07-2026
#Concatenate Non-Zero Digits and Multiply by Sum I
class Solution(object):
    def sumAndMultiply(self, n):
        concat = 0
        digit_sum = 0

        if n == 0:
            return 0

        for ch in str(n):
            digit = int(ch)
            digit_sum += digit
            if digit != 0:
                concat = concat * 10 + digit

        return concat * digit_sum

