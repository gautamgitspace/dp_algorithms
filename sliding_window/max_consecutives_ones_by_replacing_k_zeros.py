class Solution(object):
    def longestOnes(self, A, K):
        left, right, maxlen, zero_count = 0, 0, 0, 0
        while right < len(A):
            if A[right] == 0:
                zero_count += 1
                
            while zero_count > K:
                """
                time to contract the window by incrementing left as 
                we cannot accomodate more zeros acting as 'ones'
		beyond K

                While at it, we also need to decrement zero_count
                if num at left pointer is 0
                """
                
                if A[left] == 0:
                    zero_count -= 1
                left += 1
            
            maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen
