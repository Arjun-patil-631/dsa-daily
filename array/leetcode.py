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
    
    