# Problem Statement

'''

Given an integer x, return true if x is a palindrome, and false otherwise.

'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rx = x[::-1]
        if x == rx:
            return True
        return False
