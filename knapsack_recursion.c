/* 0/1 Knapsack recursion algorithm to return nax profit
 * give a weight array and value array of size n and a
 * maxium weight of the knapsack, W*/

int knapsack(weight [], value[], n, w) {
	/* base condition : always choose smallest
	 * valid value of given attributes in the
	 * problem. Here, n and w. There might be
	 * no items to pick or no capacity to put */

	if (n == 0 || w == 0)
		return 0;

	/* choice diagram translation : translate
	 * your choice diagram into code here */

	if (weight[n-1] <= w) {
		/* max of either we use that item or we not */
		return max (value[n-1] + knapsack(weight, value, n-1, w - weight[n-1]),
				     knapsack(weight, value, n-1, w));
	} else if (weight[n-1] > w) {
		/* can't use that item at all */
	    return knapsack(weight, value, n-1, w);
	}
}
