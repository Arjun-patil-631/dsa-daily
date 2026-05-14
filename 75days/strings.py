#7/5/25
#to remove the outermost parenthesis
class Solution(object):
    def removeOuterParentheses(self, s):
        result=""
        level=0
        for ch in s:
            if ch=="(":
                if level>0:
                    result+=ch
                level+=1
            if ch==")":
                level-=1
                if level>0:
                    result+=ch
                
        return result
        
#10-7-2025
#longest common prefix in an array of strings
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ans=[]
        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                return ''.join(ans)
            ans.append(first[i])
        return ''.join(ans)

#largest odd number in a string 
class Solution(object):
    def largestOddNumber(self, num):
        ind=-1
        i=0
        for i in range(len(num)-1, -1, -1):
            if (int(num[i])%2)==1:
                ind=i
                break
        i=0
        while i<=ind and num[i]==0:
            i+=1
        return num[i:ind+1]

#14-05-2025
#Isomorphic strings
class Solution(object):
    def isIsomorphic(self, s, t):
        m1, m2=[0] * 256, [0] * 256
        n=len(s)
        for i in range(n):
            if m1[ord(s[i])]!=m2[ord(t[i])]:
                return False
            m1[ord(s[i])]=i+1
            m2[ord(t[i])]=i+1
        return True
        