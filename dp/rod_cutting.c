/* ROD CUTTING PROBLEM 
 * 
 * We have a rod of given length N and two arrays length and price
 *
 * - we gotta cut this rod in parts where parts add up to N
 * - for each of these parts, we add the price associated 
 *   with these parts. 
 * - We have to maximize such profit
 * - in some cases Length array might not be given but can be derived
 *   as its just an arry of indices up to N 
 *
 * Comparing to Knapsack, here N is nothing but W hence the capacity. 
 * Length is nothing but weight arr & price array is value arr
 *
 * But this is unbounded and hence item can be re-processed to achieve
 * the max profit */


int length = {1, 2, 3, 4, 5, 6, 7, 8};
int price = {1, 5, 8, 9, 10, 17, 17, 20};
int N = 8

static int t[n + 1][length + 1];

/* INIT */
for (int i = 0; i < N + 1; i++) {
	for (int j = 0; j < length + 1; j++) {
		if (i == 0 || j == 0) {
			t[i][j] = 0;
		}
	}
}

/* TRANSLATION OF CHOICE DIAGRAM */
for (int i = 1; i < N; i++) {
	for (int j = 1; j < length; j++) {
		if (length[i - 1] <= j) {
			/* max of either we use that item (multiple times) 
			 * or we do not.
			 * -  when we use, we add its price and deduct its
			 *    length from the length array 
			 * -  when we don't we just process the item*/
			t[i][j] = max (price[i - 1] + t[i][j - length[i - 1]],
				           t[i - 1][j]);
		} else {
			/* we just process the unusable item and move on */
			t[i][j] = t[i-1][j];
		}
	}
}

return t[n][w];
