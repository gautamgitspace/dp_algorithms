# UNBOUNDED KNAPSACK PROBLEMS

- rod cutting problem
- coin change I and II
- maximum ribbon cut

# How UNBOUNDED is different from zero/one knapsack?

- in 01K, once item is processed (decision taken to include it or not)
  we don't go back to it. In unbounded, occurence of such item is 
  multiple hence we go back to the item and take an inclusion decision
  multiple times.

# How UNBOUNDED is same as 01K?

- init of 2d array is same as 01K

# CODE CHANGE?

- when item is processed, we don't go back to it in 01K
  but here we have to.

  so we do something like this:
  t[i][j] = t[i - 1][j] + t[i][j - arr[i-1]]

  i.e we process i again even if processed earlier
  
  insted of 
  t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i-1]]




