def max_eggs_collected(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])

    # Create a 2D array to store the maximum number of eggs collected at each position
    dp = [[0] * n for _ in range(m)]

    # Initialize the top-left cell
    dp[0][0] = matrix[0][0]

    # Update the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # Update the first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    # Fill in the rest of the matrix using dynamic programming
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = matrix[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    # The result is stored in the bottom-right cell
    return dp[m - 1][n - 1]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = max_eggs_collected(matrix)
print("Max eggs collected:", result)
