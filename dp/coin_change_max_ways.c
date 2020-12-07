/* You are given coins of different denominations and
 * a total amount of money. Write a function to compute
 * the number of combinations that make up that amount.
 * You may assume that you have infinite number of each
 * kind of coin. i
 *
 * this is same as subset sum problem/ count of subset
 * sum but for unbounded K
 * */

int coins = [1, 2, 5];
int amount = 5;

int n = sizeof(coins) / sizeof(int);
int dp[n + 1][amount + 1];

 /* INIT */
 for (int i = 0; i < n + 1; i++) {
 	for (int j = 0; j < amount + 1; j++) {
 		if (i == 0) {
 			dp[i][j] = 0;
 		}
 		if (j == 0) {
 			dp[i][j] = 1;
 		}
 	}
 }

 /* translation of choice diagram */
 for (int i = 1; i < n; i++) {
 	for (int j = 1; j < amount; j++) {
 		/* item cannot be picked so just process it */
 		dp[i][j] = dp[i - 1][j];
 		if (coins[i - 1] <= j) {
 			/* item can be picked. Here we do not take 'OR'
 			 * but we add both choices - do we pick, do we not
 			 * this is done cause we might not pick 2,3,5 and
 			 * just pick 10 alone which in turn solves our
 			 * purpose. So all such cases need to be counted */
 			dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j];
		}
 	}
 }
