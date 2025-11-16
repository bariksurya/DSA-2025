'''
count the no of subset in the array which difference is same as given difference

trick :

S1-S2 = diff
S1+S2 = Stotal

S1 = (Stotal+diff)/2
'''

def count_no_of_subset_of_given_diff(arr, diff):
    n = len(arr)
    total_sum = sum(arr)
    # Check for valid partition
    if (diff + total_sum) % 2 != 0 or diff > total_sum:
        return 0
    target = (diff + total_sum) // 2

    # Allocate DP table the right size NOW
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Initialize: There's always 1 way to get sum 0 (empty subset)
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]


# Example usage:
arr = [1, 2, 3, 1, 2]
diff = 1
print(count_no_of_subset_of_given_diff(arr, diff))  # Output: 5