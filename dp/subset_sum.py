#!/usr/bin/env python

'''
find if a subset exists in a array
that sums up to a given target k

arr = [2,3,7,8,10] 
sum = 11 
output = True

2d bottom-up Knapsack DP
'''
class Solution:
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
    nums = [2,3,7,12,10]
    print (s.does_exist_subset(nums, 5))
