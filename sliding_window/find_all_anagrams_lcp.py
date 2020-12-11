#!/usr/bin/env python

"""
Given a string s and a non-empty string p, find
all the start indices of p's anagrams in s.

this times out for large outpute due to slowness
of counters.
"""

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        l, r, ret = 0, 0, []
        
        while r < len(s):
            if r - l + 1 < len(p):
                r += 1
            elif r - l + 1 == len(p):
                if Counter(s[l : r + 1]) == Counter(p):
                    ret.append(l)
                l += 1
                r += 1
        return ret

    def findAnagrams_optim(self, s, p):
        res = []
        k = len(p) # fixed window size
        
        pCounter = Counter(p)
        sCounter = Counter(s[: k - 1])
        
        for right in range(k - 1, len(s)):
            # expand window or add new char to window
            sCounter[s[right]] += 1
            
            if sCounter == pCounter:
                # compare alphas of s with p and append idx
                # basically idx here is left and we know that
                # right - left + 1 = k (WS) which implies:
                # right - k + 1 = left
                res.append(right - k + 1)      
            
            # deduct from map the count of the oldest char
            sCounter[s[right - k + 1]] -= 1
            
            # if it becomes 0, remove it from the map
            if sCounter[s[right - k + 1]] == 0:
                del sCounter[s[right - k + 1]]
        return res

