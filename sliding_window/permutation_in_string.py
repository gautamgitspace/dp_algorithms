"""
Exactly similar to find all anagrams LCP #438
here p = s1 and s = s2. Second solution is 
more intuitive and likely to hit the brain
in an interview but times out for unrealistic
inputs.
"""
from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        k, size = len(s1), len(s2)
        
        s1_counter = Counter(s1)
        s2_counter = Counter(s2 [: k - 1])
        
        print s1_counter
        print s2_counter 
        
        for R in range(k - 1, size):
            s2_counter[s2[R]] += 1              # add new char to the window
            
            if s2_counter == s1_counter:        # comparison
                return True                     # we done here once this holds
            s2_counter[s2[R - k + 1]] -= 1      # R - L + 1 = k => R -k + 1 = L
            
            if s2_counter[s2[R - k + 1]] == 0:
                del s2_counter[s2[R - k + 1]]   # update map (process on left)
        return False
        
        
        
    def checkInclusion2(self, s1, s2):
        """
        times out for unrealistic inputs =[
        """
        k, size = len(s1), len(s2)
        left, right = 0, 0
        
        while right < size:
            if right - left + 1 < k:
                right += 1
            elif right - left + 1 == k:
                if Counter(s1) == Counter(s2[left : right + 1]):
                    return True
                left += 1
                right += 1
        return False
