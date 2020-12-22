class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        - variable window size, so we gotta maintain
        - condition sum >= s yields candidate answer
	- since its >= everything after this condition
	  is met, could be the answer => while loop
        """
        left, right = 0, 0
        sums, min_len = 0, len(nums) + 1
        
        for right, item in enumerate(nums):
            sums += item
            while sums >= s:
                # condition hit, calculate
                min_len = min(min_len, right - left + 1)
                
                # deduct from left
                sums -= nums[left]
                
                # contract window
                left += 1
        return min_len if min_len <= len(nums) else 0
