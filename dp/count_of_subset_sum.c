/* Now we have to count the number of subsets that exist in the given
 * array that sum to up to a given sum. So count of all such 'True' 
 * instances returned by subset sum problem. So here return type is int */

int arr = {2, 3, 5, 6, 8, 10};
int sum = 10;

int n = sizeof(arr) / sizeof(int);
int t[n + 1][sum + 1];

/* INIT */
for (int i = 0; i < n + 1; i++) {
	for (int j = 0; j < sum + 1; j++) {
		if (i == 0) {
			t[i][j] = 0;
		}
		if (j == 0) {
			t[i][j] = 1;
		}
	}
}

/* translation of choice diagram */
for (int i = 1; i < n + 1; i++) {
	for (int j = 1; j < sum + 1; j++) {
		if (arr[i - 1] <= j) {
			/* item can be picked. Here we do not take 'OR'
			 * but we add both choices - do we pick, do we not
			 * this is done cause we might not pick 2,3,5 and
			 * just pick 10 alone which in turn solves our
			 * purpose. So all such cases need to be counted */
			t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j];
		} else {
			/* item cannot be picked, but is processed */
			t[i][j] = t[i - 1][j];
		}
	}
}

return t[n][sum];
