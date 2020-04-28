/* Bottom up approach. we start with the tabular matrix approach
 * by initializing matrix using base case and then build the soln
 * to the top 
 *
 * - init the matrix with -1 at all values as before
 * - we omit the recursive call and just use the matrix.
 *   Change the calls to iterative.
 * - derive bottom-up code from recursive */


static int t[n+1][w+1];

/* base condition changes to initialization */
for (int i = 0; i < n + 1; i++) {
	for (int j = 0; J < w + 1; j++) {
		if (i == 0 || j == 0) {
			t[i][j] = 0;
		}
	}
}

for (int i = 0; i < n + 1; i++) {
	for (int j = 0; j < w + 1; j++) {
		if (weight[i-1] <= j) {
			/* max of either we use that item or we not
			 * - when we use the item, we add its value and
			 * 	 subtract its weight from w
			 * - when we don't use the item, we just process
			 *   it*/
			t[i][j] = max(val[i-1] + t[i-1][j] - weight[i-1],
					      t[i-1][j]);
		} else {
			/* we just process item, don't use it */
			t[i][j] = t[i-1][j];
		}
	}
}

return t[n][w];
					      

