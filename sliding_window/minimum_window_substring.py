class Solution(object):
    def minWindow(self, s, t):
        """
        TEST INPUT:
        
        s = "ADYBACGG"
        t = "ABC"
        
        #0: keep a map of chars in t
        
        #1: must_have_char_count is the bare necessity substr
            that should exist in s to fulfill the criteria
        
        #2: it's a hit. we found one of the bare necessary char
        
        #3: all hits completed (all bare necessary chars found)
            at this point we calculate in what window length did
            we manage to do this? this would be r - l + 1 and if
            this is LT MWL, we update MWL.
        
        #4: Our work is not done right now. We found 'BAC' in
            'ADYBAC' as a best effort. but now we gotta trim it
            to just 'BAC' as that's more optimal.
            
            Now here we take care of desired character and get
            rid of 'extra' by setting must_have_char_count > 0
            For this input, the first 'A'is 'extra' and can be
            ignored. We move on further and select smaller window
            i.e. 'BAC'
        
        #5  Setting this will help us get out of the nested while.
            We only do it for chars have +ve count. 'A' in this case
            is extra and would revive from a -ve count first
        
        #6: keep contracting window. 'D' and 'Y' are of no use to us
            also we gotta reach 'BAC' i.e. a smaller window
        
        #7: keep expanding in search of new (tha basics)
        """
        freq = {}
        for char in t:                                          #0
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        left, right, must_have_char_count = 0, 0, len(t)        #1
        mwl, mws = len(s) + 1, 0
        
        while right < len(s):
            if s[right] in freq:                                #2
                if freq[s[right]] > 0:
                    must_have_char_count -= 1
                freq[s[right]] -= 1
            
            while must_have_char_count == 0:                    #3
                if right - left + 1 < mwl:
                    mwl = right - left + 1
                    mws = left

                if s[left] in freq:                             #4
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:                       
                        must_have_char_count += 1               #5
                left += 1                                       #6
            right += 1
        
        return "" if mwl == len(s) + 1 else s[mws : mws + mwl]
