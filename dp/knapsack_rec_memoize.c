/* Now we memoize the recursive solution for knapsack :

 * In the recursive function we wrote for knapsack before,
 * some inputs args change with iterations but some do not.
 * We are gonna consider inputs that change as we process.
 * 
 * For instance, n and w were changing. So n and w will be 
 * the two dimensions for our DP matrix : t[n+1] [w+1]. we
 * init this by -1 for all grid values.
 *
 * Next, we gotta check if the grid value returned by our
 * recursive function returns some valid value (sub-prob
 * soln). This will be reused. Or if it returns -1 (we 
 * compute the sub-prob soln this time and memoize/store 
 * it for next time use). */

static int t[n + 1][w + 1];
memset(t, -1, sizeof(t));

int knapsack(weight [], value[], n, w) {
  if (n == 0 || w == 0)
		return 0;

  if (t[n][w] != -1) {
    /* sub-prob soln, we have some
     * grid value, we reuse it */
    return t[n][w];
  }
  /* otherwise we recurse and memoize */
  if (weight[n - 1] <= w) {
		/* max of either we use that item or we not, memoize this rec call there and then */
		return t[n][w] = max (value[n - 1] + knapsack(weight, value, n - 1, w - weight[n - 1]),
				     knapsack(weight, value, n - 1, w));
	} else if (weight[n - 1] > w) {
		/* can't use that item at all, memoize at the same time */
	    return t[n][w] = knapsack(weight, value, n - 1, w);
	}
}
