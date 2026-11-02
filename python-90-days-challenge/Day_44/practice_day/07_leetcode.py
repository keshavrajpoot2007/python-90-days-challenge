# Problem Statement

'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

'''

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)
        
