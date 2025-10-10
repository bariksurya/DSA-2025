'''
Given a set of non-negative integers and a target sum, 
determine if there exists a subset of the set 
whose sum is exactly equal to the target.

For example, given the set [3][34][4][12][5][2] and target sum 9, 
the answer is True because the subset [4][5] sums to 9.
'''

'''
1. Create a DP matrix of size (n+1) x (sum+1) initialized to False.
2. Set the first column to True (sum 0 is always possible).
3. For each element and each possible sum, fill the matrix using the recurrence:
    If the current element is greater than the sum, 
    copy the value from above.
    Otherwise, set the cell to True if either the sum can be 
    achieved without the current element or by including it.
'''

def is_subset_sum(arr,sum):
    n = len(arr)
    # create a 2D dp arr
    # dp matrix n+1 row, sum+1 col
    dp = [[False]*(sum+1) for _ in range(n+1)]

    '''
    If n = 2 and sum_value = 3, the result is:
    [False, False, False, False],  # row 0
    [False, False, False, False],  # row 1
    [False, False, False, False]   # row 2
    '''

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                  
    return dp[n][sum]


arr = [3, 34, 4, 12, 5, 2]
sum = 7
print(is_subset_sum(arr, sum))