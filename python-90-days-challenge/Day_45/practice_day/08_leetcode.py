# Problem Statement

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
    
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]