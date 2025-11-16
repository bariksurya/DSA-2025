'''
Find the minimum subset in an array in which minimum absolute difference of both the sum is minimum.

Given a set of integers, split it into two subsets such that the absolute difference between the subset sums is as small as possible.

Step-by-step Solution Outline

1. Calculate total sum.
2. S1 and S2 will fall between range 0->S/2 

S2 = range-2s1 -> will always be abasolute if we take S1 will lie between 0->sum/2

3. in dp calculate the last row of subset sum problem
4. last row take as a vector and see which sum is possible upto range/2
5. then find s2 with formula

'''

def min_subset_sum_difference(arr):
    total_sum = sum(arr)
    n = len(arr)
    dp = [[False]* (total_sum+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, total_sum+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp [i-1][j-arr[i-1]]

    for j in range(total_sum//2,-1,-1):
        if dp[n][j]:
            min_diff = abs(total_sum-2 * j)
            return min_diff
            break

arr = [1, 9, 2, 3]
print(min_subset_sum_difference(arr))  # Output: 1
