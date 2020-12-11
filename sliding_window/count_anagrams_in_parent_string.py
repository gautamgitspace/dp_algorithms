#!/usr/bin/env python

from collections import Counter

"""
Given string S and a pattern P, find anagrams
of P in S. Here basically size of P is k and 
hence fixed window size and anagram is nothing
but a continuous subarray we need to find
"""

def count_anagrams(s, p):
    left, right, count, k = 0, 0, 0, len(p)

    while right < len(s):
        if right - left + 1 < k:
            right += 1
        elif right - left + 1 == k:             # window hit
            if Counter(s[left : right + 1]) == Counter(p):
                count += 1
            left += 1
            right += 1
    return count

if __name__ == '__main__':
    s = 'rofor'
    p = 'for'
    print count_anagrams(s, p)
