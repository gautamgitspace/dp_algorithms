"""
Sliding Window. Type : fixed window size

- here window size is fixed i.e. size of subarray

- once we reach k, we maintain the size and keep
  finding max of computed sum

- again we start with two ptrs - left and right
"""

def max_sum_subarray_of_size_k(self, nums):
    left, right, sums = 0, 0, 0

    while right < len(nums):
        sums += nums[right]                 # compute sum/process on right

        if right - left + 1 < k:            # expand window
            right += 1
        
        elif right - left + 1 > k:          # window size hit
            maximum = max(maximum, sums)    # compute maximum
            sums -= nums[left]              # deduct from sums/process on left
            i += 1                          # move window (left)
            j += 1                          # move window (right)
    
    return maximum
