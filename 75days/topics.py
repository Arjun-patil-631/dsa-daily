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