/* Given an array, we have to find all such partitions whose difference comes out
 * to be the given difference *
 *
 * partitions p1 and p2 will have sums s1 and s2 and we have to find count of all
 * such pairs such that s1 - s2 = diff OR s2 - s1 = diff 
 *
 * it's clearly evident that : 		  s1 + s2 = sum(arr) 
 * From before we know we gotta find: s1 - s2 = diff
 *
 * if we add above two statments : 	  2s1 = diff + sum(arr) 
 * or we can say that: 				  s1 = (diff + sum(arr)/2) 
 *
 * now s1 can we calculated since we diff & sum(arr) can be calculated 
 *
 * This meanns we will have something like s1 = value 
 * so we gotta find some subsets in arr that sum up to value! 
 * This has been reduced to count of subset sum problem */


int arr = {1, 1, 2, 3};
int diff = 1;
int sum = 0;

int n = sizeof(arr) / sizeof(int);

for (int i = 0; i < n; i++) {
	sum += arr[i];
}

/* now we have sum(arr) i.e. sum and diff 
 * so we will calculate s1 as explained */

s1_sum = (diff + sum)/2;

/* now we gotta find count of subsets 
 * that sum up to s1_sum */

int t[n + 1][s1_sum + 1];

/* INIT 
 * t[0][j] -> no item picked but sum can be 0,1, ...  s1_sum. this can't be done. 
 * t[i][0] -> items can be picked 1 to n but s1_sum has to be 0. So we pick null set*/
for (int i = 0; i < n + 1; i++) {
	for (int j = 0; j < s1_sum + 1; j++) {
		if (i == 0) {
			t[i][j] = 0;
		} else if (j == 0) {
			t[i][j] = 1;
		}
	}
}

/* translation of choice diagram */
for (int i = 1; i < n + 1; i ++) {
	for (int j = 1; j < s1_sum + 1; j++ ) {
		if (arr[i - 1] <= j) {
			/* item can be picked 
			 * - we pick and subtract its weight 
			 * - we do not pick but just process*/
			t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j];
		} else {
			/* item cannot be picked, but is processed
			 * and we move on to the next eligible item*/
			t [i][j] = t[i - 1][j];
		}
	}
}

return t[n][s1_sum];
