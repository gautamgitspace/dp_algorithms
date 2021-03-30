/* Bottom up approach. we start with the tabular matrix approach
 * by initializing matrix using base case and then build the soln
 * to the top 
 *
 * - we omit the recursive call and just use the matrix.
 *   Change the calls to iterative.
 * - derive bottom-up code from recursive */

/* n rows and w cols */
static int t[n + 1][w + 1];

/* base condition changes to initialization 
 * first row and first col are set to zero */
for (int i = 0; i < n + 1; i++) {
	for (int j = 0; J < w + 1; j++) {
		if (i == 0 || j == 0) {
			t[i][j] = 0;
		}
	}
}

for (int i = 1; i < n + 1; i++) {
	for (int j = 1; j < w + 1; j++) {
		if (weight[i - 1] <= j) {
			/* can use item - take it or leave it?
			 * max of either we take it or we leave it
			 * - when we take it, we add its value and
			 * 	 subtract its weight from total available w
			 * - when we leave the item, we just process
			 *   it*/
			t[i][j] = max(val[i - 1] + t[i - 1][j - weight[i - 1]],
					      t[i - 1][j]);
		} else {
			/* we just process item, can't use it (don't subtract from w) */
			t[i][j] = t[i - 1][j];
		}
	}
}

return t[n][w];
					      

