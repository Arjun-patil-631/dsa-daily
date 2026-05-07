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
        