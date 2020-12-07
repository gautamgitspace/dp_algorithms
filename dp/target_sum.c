/* mark array elements with + or - such that elements of a given array sum up to
 * the given target sum. Return the count of such combination of marked elements
 * that sum up to given target sum
 * 
 * basically this is same as finding subsets p1 and p2 with sums s1 and s2 and 
 * finding s1 - s2 = target OR s2 - s1 = target
 *
 * again, 
 *
 * s1 + s2 = sum(arr)
 * s1 - s2 = diff
 * -----------------
 * 2s1 = diff + sum(arr) => s1 = (diff + sum(arr))/2  */

int arr = {1, 1, 2, 3};
int target = 1;
int sum = 0;

int n = sizeof(arr) / sizeof(int);

for (int i = 0; i < n; i++) {
	sum += arr[i];
}

/* now we have sum(arr) and diff (give) 
 * so we calculate s1 as explained above */

s1_sum = (diff + sum)/2;

/* now we find count of all such subsets 
 * that sum up to s1_sum */

count = count_of_subsets(n, s1_sum);

return count;
