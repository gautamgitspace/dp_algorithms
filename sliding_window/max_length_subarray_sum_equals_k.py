"""
same as subarray sum equals k. in that we used to
return the number of such subarrays whose sum used
to equal k.

Here, we return the max len of one such subarray
that sums up to k.

clearly we need to play with index here. whenever
d.get(sums - k) fulfills the criteria, we need to
track the index. basically we need to track from
where the stretch begins and until where it lasts

PS - we discussed what a stretch is previously
"""

def max_sub_array_len_sum_equals_k(self, nums, k):
    d = {0 : -1}
    sums = max_len = 0
    for i in range(len(nums)):
        sums += nums[i]
        if sums - k in d:
            max_len = max(max_len, i - d[sums - k])
        # store the index
        d[sums] = i
    return max_len

"""
Using sliding window:

- condition given: sum should equal k (yields candidate answer)

- window size not given: variable

- right moves in all three conditions

- unlike fixed window, here we take care of one more condition
  i.e. sums > k. as in fixed window case, we maintain the size
  but here we have no control over the sum and it will keep on
  stockpiling if we not deduct from the left
"""
def max_sub_array_len_sum_equals_k(self, nums, k):
    left, right, sums, max_size = 0, 0, 0, - float('inf')

    while right < len(nums):
        sums += nums[right]
        if sums < k:
            right += 1
        elif sums == k:
            max_size = max(max_size, right - left + 1)
            right += 1
        elif sums > k:
            while sums > k:
                sums -= nums[left]
                left += 1
            right += 1
    return max_size
