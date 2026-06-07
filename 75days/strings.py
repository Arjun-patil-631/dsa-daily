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
        
#reverse words in a string
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

#15-05-2025
#anagram of a string
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        freq=[0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        for ch in t:
            freq[ord(ch)-ord('a')]-=1
        for count in freq:
            if count!=0:
                return False
        return True

#maximum nesting depth of a parentheses string
class Solution(object):
    def maxDepth(self, s):
        p=0
        ans=0
        for ch in s:
            if ch=='(':
                p+=1
            elif ch==')':
                p-=1
            ans=max(ans, p)
        return ans
            
#roman to integer
class Solution(object):
    def romanToInt(self, s):
        roman={
            'I':1,'V':5,'X':10,'L':50,
            'C':100,'D':500,'M':1000
        }
        res=0
        l=len(s)
        for i in range(l):
            if i<l-1 and roman[s[i]]<roman[s[i+1]]:
                res-=roman[s[i]]
            else:
                res+=roman[s[i]]
        return res
        
#16-05-2025
#longest palindromic substring
class Solution(object):
    def longestPalindrome(self, s):
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        ans=""
        for i in range(len(s)):
            p1=expand(i,i)
            p2=expand(i,i+1)
            if len(p1)>len(ans):
                ans=p1
            if len(p2)>len(ans):
                ans=p2
        return ans

#19-05-2025
#longest substring without repeating characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen={}
        left=0
        max_len=0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]]>=left:
                left=seen[s[right]]+1
            
            seen[s[right]]=right
            max_len=max(max_len, right-left+1)
        return max_len

#20-05-2025
#string compression
class Solution(object):
    def compress(self, chars):
        s=[]
        temp=chars[0]
        count=0
        for char in chars:
            if char==temp:
                count+=1
            else:
                s.append(temp)
                if count>1:
                    s.extend(str(count))
                temp=char
                count=1
        s.append(temp)
        if count>1:
            s.extend(str(count))
        chars[:len(s)]=s
        return len(s)
            
#22-05-2026
#valid palindrome
class Solution(object):
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True

#29-05-2026
#index of first occurrence in a string
#my method using slicing
class Solution(object):
    def strStr(self, haystack, needle):
        i,leng=0,len(needle)
        for i in range(len(haystack)-leng+1):
            if haystack[i:i+leng]==needle:
                return i
        return -1
#using inbuilt function good for time complexity 
class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
#giives same time complexity as above but similar to my method
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            if haystack[i:i +  m] == needle:
                return i
        return -1

#30-05-2026
#intger to roman
class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]

        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]
        ans=[]
        for i in range(len(values)):
            while num>=values[i]:
                ans.append(symbols[i])
                num-=values[i]
        return "".join(ans)

#05-06-2026
#removing stars from a string
class Solution(object):
    def removeStars(self, s):
        stack=[]
        for ch in s:
            if ch=='*':
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

#06-06-2026
#length of last word in a string
class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.split()
        if not words:
            return 0
        return len(words[-1])
#for interview purpose without using split
class Solution(object):
    def lengthOfLastWord(self, s):
        length=0
        i=len(s)-1
        while i>=0 and s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1
        return length
    
#07-06-2026
#string to integer(atoi)
INT_MIN=-2**31
INT_MAX=2**31-1
def helper(s,i,num,sign):
    if i>=len(s) or not s[i].isdigit():
        return sign*num
    num=num*10+int(s[i])

    if sign*num>=INT_MAX: 
        return INT_MAX
    if sign*num<=INT_MIN: 
        return INT_MIN

    return helper(s,i+1,num, sign)

class Solution(object):
    def myAtoi(self, s):
        i=0
        while i<len(s) and s[i]==' ':
            i+=1
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        return helper(s, i, 0, sign)
        
            
