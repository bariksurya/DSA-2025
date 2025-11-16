'''
The Equal Sum Partition problem asks whether you can partition an array 
into two subsets such that the sum of elements in both subsets is equal.

To get two equal partition the sum of array element will alwways should be even.

Solution:
Calculate the total sum: If the sum is odd, return false immediately 
since you cannot divide an odd number into two equal integers.

Find subset with target sum: If the sum is even, find whether there exists a 
subset with sum equal to total_sum/2, total_sum/2 using the subset sum algorithm

'''

def is_equal_partion(arr):
    total = sum(arr)
    if total%2 != 0:
        return False
    else:
        return is_subset_sum(arr,total//2)

def is_subset_sum(arr,sum):
    n = len(arr)

    dp = [[False]*(sum+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                  
    return dp[n][sum]

# arr = [3, 34, 4, 12, 5, 2]
arr = [1, 5, 11, 5]
print(is_equal_partion(arr))