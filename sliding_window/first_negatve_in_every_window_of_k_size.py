#!/usr/bin/env python

"""
BRUTE FORCE APPROACH

- use two ptrs and walk the damn array
"""

def first_negative_in_every_window_bf(nums, k):
    ret = []
    for i in range(len(nums) - k + 1):
        found_negative = False
        for j in range(0, k):
            if nums[i + j] < 0:
                found_negative = True
                ret.append(nums[i + j])
                break
        if not found_negative:
            ret.append(0)

    return ret

"""
SLIDING WINDOW APPROACH, avoiding rework
of evaluating if a number in nums is -ve
"""

def first_negative_in_every_window_optimized(nums, k):
    left, right = 0, 0
    temp, ret = [], []
    
    while right < len(nums):
        if nums[right] < 0:
            temp.append(nums[right])            # store the negative number/process on right
        
        if right - left + 1 < k:                # expand window
            right += 1
        
        elif right - left + 1 == k:             # window size hit
            if len(temp) == 0:                  # case when no negative num was encountered
                ret.append(0)
            else:
                ret.append(temp[0])             # normal case when negative was encountered
                                                # the very first negative num added to temp
                                                # is our guy to be included in ret
                
                if nums[left] == temp[0]:       # deduction from window. if num at left is
                                                # also present in our temp in the begining
                                                # we deduct it by deleting it/proces on left
                    del temp[0]

            right += 1                          # slide window (right)
            left  += 1                          # slide window (left)

    return ret


if __name__ == "__main__":
    nums = [12, -1, 7, 8, 15, -30, 16, 28]
    print first_negative_in_every_window_bf(nums, 3)
    print first_negative_in_every_window_optimized(nums, 3)
