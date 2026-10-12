# Problem Statement

'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        s = s.strip("-")
        s = s[::-1]
        if x > 0:
            x = int(s)
        else:
            x = int(s)
            x *= -1

        if -2**31 <= x <= 2**31 - 1:
            return x
        else:
            return 0

