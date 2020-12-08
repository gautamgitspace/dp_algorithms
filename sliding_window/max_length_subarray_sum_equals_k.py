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
