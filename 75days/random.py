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
    
