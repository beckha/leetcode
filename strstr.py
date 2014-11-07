# -*- coding: utf-8 -*-


class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        length_hay = len(haystack)
        length_nee = len(needle)
        for i in range(length_hay - length_nee):
            if haystack[i:i+length_nee] == needle:
                return i
        return -1
