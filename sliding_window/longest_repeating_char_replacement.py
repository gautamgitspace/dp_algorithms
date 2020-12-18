class Solution(object):
    def characterReplacement(self, s, k):
        d = collections.defaultdict(int)
        left, result, most_freq = 0, 0, 0
        
        for right in range(len(s)):
            d[s[right]] += 1
            # keeping max at all times
            most_freq = max(most_freq, d[s[right]])     

            """
            at any time in a window size, we would want to
            know the letters we want to replace. letters
            to replace will be calculated by:
            
            current WS - most frequent char in the window
            
            WHY? because this will give us the remaining
            least frequent occurring letters which can be
            replaced.
            
            now once we know the num of letters to be 
            replaced, we need to keep them under k or
            we have a violation. When it exceeds k, we
            would need deduction and window contraction
            """
            # when letters to be replaced  GT k
            if right - left + 1 - most_freq > k:
                d[s[left]] -= 1                     # deduction
                left += 1                           # contract window
            result = max(result, right - left + 1)
        
        return result
