4-7-2026
#linked list cycle 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow

#5-07-2026
#isomorphic strings
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

#contains duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

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

#23-07-2026
#contains duplicate 2
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        s = set()

        for i in range(len(nums)):
            if nums[i] in s:
                return True

            s.add(nums[i])

            if len(s) > k:
                s.remove(nums[i - k])

        return False
    
#above solution is not optimal as it uses set and remove operation takes O(n) time in worst case. 
#below is optimal solution using dictionary which takes O(1) time for insert and lookup operation.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False
