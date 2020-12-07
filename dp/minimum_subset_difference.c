/* Given an array, we have to find two partitions of the array such that
 * the abs difference of the partitions is minimum */

/* For instance, here we can consider two sets: {1, 6, 5} and {11} and 
 * minimum abs diff of them to be 1. To generalize, we have to find two
 * partitions p1 and p2 with sum s1 and s2 such that s2 - s1 = minimum
 * assuming that s1 lies to the left of number line i.e. s2 is bigger */

/* Now, HOW TO pick p1 & p2 and hence s1 & s2?
 * We know that s1 and s2 lie between 0 and a range that is sum(arr[i])
 * So on a number line it will be something like:
 *
 * 			0--------s1---|---s2------range 
 * 
 * So we can say that if p1 has sum s1, then p2 will have sum (range - s1)
 * Now coming back to the problem, we gotta minimize (s2 - s1). if we 
 * subsitute s2 with 'range - s1' we establish that we gotta minimize 
 * (range - 2(s1)) 
 *
 *
 * Now HOW TO find s1? What are s1 candidates? We do know that they lie 
 * between 0 to range. Also that list can be pruned based on given input
 * For instance, if arr = [1, 2, 7], candidates for s1 will only be those
 * numbers on the number line which are a subset sum formed by elements
 * of arr. So this can be reduced to a subset problem (arr, range)
 * For this example 4, 5, 6 can be pruned from s1 candidates as elements
 * in arr cannot form a subset sum of 4, 5 and 6.
 * */

int* subset(int *pruned[], int arr[], int range, int n);

/* prune list of s1 candidates using subset problem */
int* subset(int *pruned[], int arr[], int range, int n) {
	int t[n + 1][range + 1];
	/* INIT */
	for (int i = 0; i < n + 1; i++) {
		for (int j = 0; j < range + 1; j++) {
			if (i == 0) {
				t[i][j] = false;
			} else if (j == 0) {
				t[i][j] = true;
			}
		}
	}

	/* translation of choice diagram */
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < sum + 1; j++) {
			if (arr[i - 1] <= j) {
				/* item can be picked */
				t[i][j] = t[i - 1][j] || t[i - 1][j - arr[i - 1]];
			} else {
				/* item can't be picked just process it */
				t[i][j] = t[i - 1][j];
			}
		}
	}
	/* now we gotta fill the prune list using the last row of the
	 * t matrix. these are the s1 candidates, obtained by leveraging
	 * the subset problem. We only do it till half as we are assuming
	 * that s1 lies in the left half and s2 lies in the right half */

	for (int i = 0; i < range/2; i++) {
		if (t[n][i]) {
			pruned [i] = t[n][i];
		}
	}
 return pruned;
}

int main() {
	int arr [] = {1, 6, 11, 5};
	int n = sizeof(arr) / sizeof(int);
	int range = 0;
	int min_ret = INT_MAX;

	for (int i = 0; i < n; i++) {
		range += arr[i];
	}

	int pruned[range/2];
	
	int* s1_candidates = subset(pruned[], arr[], range, n);

	for (int i = 0; i < s1_candidates.size() ; i++) {
		min_ret = min(min_ret, range - (2 * s1_candidates[i]));
	}

	return min_ret;
}

