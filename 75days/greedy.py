#day-1
#what is greedy algorithm?
#greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally
#optimal choice at each stage with the hope of finding a global optimum. In other words, it makes the best choice
#at each step without considering the consequences of that choice on future steps. Greedy algorithms are often used
#for optimization problems where the goal is to find the best solution among a set of possible solutions.
#However, greedy algorithms do not always guarantee an optimal solution, and they may fail to find the best solution in
#some cases. Therefore, it is important to analyze the problem and determine whether a greedy approach is appropriate 
# before using it.

#30-5-2026
#LC55
#Jump Game
class Solution(object):
    def canJump(self, nums):
        maxi=0
        for i in range(len(nums)):
            if i>maxi:
                return False
            maxi=max(maxi, i+nums[i])
        return True
