/* partition of array of into halves such that they have equal sum
 * return TRUE if 2 such partitions are possible, else return FALSE */

/* given - arr */

/* this is very similar to subset sum problem as in both the problems 
 * we gotta find subsets (partitions) */

/* technically if we have 2 partitions say p1 & p2 with sums s1 & s2,
 * and if we NEED s1 == s2, then sum of array is 2s1 or 2s2 which means
 * array sum is even (anything multiplied by 2) So this task is only
 * doable when array sum is EVEN 
 *
 * also if we can find s1, s2 essentially needs to be same as s1. So we've
 * reduced this problem to subset sum problem - find a subset in given arr
 * that sums up to half of k
 *
 * PS - this is also solvable using the leftsum and rightsum approach */

int n = sizeof(arr) / sizeof(int);
int sum = 0;

/* find running sum */
for (int i = 0; i < n; i++) {
	sum += arr[i];
}

if (sum % 2 != 0) { return false;}
else if (sum % 2 == 0) { return subset_sum(arr, sum/2);}
