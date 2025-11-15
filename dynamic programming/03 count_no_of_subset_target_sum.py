'''
No of subset present in the array which sum is equal to given sum input

Tricks:
Initialize the DP Table: Set all values to 0, 
except for sum 0 (which is always possible by picking nothing).

Iterate Over the Array: For each element, for each possible sum 
from 0 to target,
If you exclude the element, the count is unchanged.
If you include it (if possible), add the count from the dp cell 
that sums to j - arr[i-1].

Result: dp[n][target] gives the answer.

'''

def count_no_of_subset_of_given_sum(arr,sum):
    n = len(arr)
    # 2D matrix with n+1, sum+1

    dp = [[0] * (sum + 1) for _ in range(n + 1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,sum+1):
             # Exclude current element
            dp[i][j] = dp[i - 1][j]
            # Include it (only if it doesn't exceed current sum)
            if j >= arr[i - 1]:
                dp[i][j] += dp[i - 1][j - arr[i - 1]]
        
    return dp[n][sum]


arr = [1, 2, 3, 3]
target = 6
print(count_no_of_subset_of_given_sum(arr, target))
