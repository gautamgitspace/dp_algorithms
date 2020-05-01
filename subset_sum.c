/* find if a subset exists in a array that sums up to a given target sum */

/* arr = [2,3,7,8,10] 
 * sum = 11 */

/* WHY DP?
 * - We have a choice for numbers, should we include
 *   an item to be a part of the sum or not 
 * - We have a max target to meet */

int n = sizeof(arr) / sizeof(int);
int t[n+1][sum+1];

/* what to return? T or F, so that's 
 * what we'll init the matrix with 
 * - t[0][0] will be true, empty set
 * - t[1][0] will be true as well. so on until t[n+1][0]
 * - t[0][1] won't be true. Sum can't be 1 when no item to be picked 
 * - t[0][2] won't be true as well. so on until t[0][sum+1]*/

/* INIT */
for (int i = 0; i < n + 1; i++) {
	for (int j = 0; j < sum + 1; sum++) {
		if (i == 0) {
			t[i][j] = false;
		} 
		else if (j == 0) {
			t[i][j] = true;
		}
	}
}

/* translation of choice diagram */
for (int i = 0; i < n + 1; i++) {
	for (int j = 0; j < sum + 1; j++) {
		if (arr[i - 1] <= j) {
			/* item can be picked. case for do we pick || do we not. 
			 * when we do, we process and subtract its value from sum
			 * when we do not, we just process */
			t[i][j] = t[i - 1][j - arr[i - 1]] || t[i - 1][j];
		} else {
			/* we just process and not use it*/
			t[i][j] = t[i - 1][j];
		}
	}
}
return t[n][sum];
