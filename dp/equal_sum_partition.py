#!/usr/bin/env python
'''
divide the given list into 2 subsets such that 
sum of these two subsets comes out to be k

return True if such a division is possible

this is very similar to subset sum problem as in
both the problems  we gotta find subsets. HOW:

technically if we have 2 partitions say p1 & p2
with sums s1 & s2, and if we NEED s1 == s2, then
sum of array is 2s1 or 2s2 which means array sum
is even (anything multiplied by 2) So this task
is only doable when array sum is EVEN 

Also if we can find s1; s2 essentially needs to 
be same as s1. So we've reduced this problem to
subset sum problem - find a subset in given arr
that sums up to half of k

PS - this is also solvable using the leftsum and
rightsum approach
'''

class Solution:
    def func(self, nums, k):
        prefix_sum = sum(nums)
        if prefix_sum % 2 == 0:
            return self.does_exist_subset(nums, prefix_sum / 2)
        return False

    def does_exist_subset(self, nums, k):
        n = len(nums)
        dp = [[None for _ in range (k + 1)] for _ in range (n + 1)]

        # init
        for i in range(n + 1):
            for j in range(k + 1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True

        # choice diagram translation
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if nums[i - 1] <= j:
                    # item can be picked. we either
                    # pick + process OR just process
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    # item cannot be picked as item GT k
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[n][k]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4, 2, 7]
    print(s.func(nums, 11))