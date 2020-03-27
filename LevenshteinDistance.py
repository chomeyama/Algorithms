""" s1 と s2 のレーベンシュタイン距離を求める """

def Levenshtein_Distance(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1 + 1):
        dp[i][0] = i
    for j in range(n2 + 1):
        dp[0][j] = j
    for i in range(n1):
        for j in range(n2):
            dp[i+1][j+1] = dp[i][j] + (s1[i] != s2[j])
            if dp[i][j+1] < dp[i+1][j]:
                m = dp[i][j+1] + 1
            else:
                m = dp[i+1][j] + 1
            if m < dp[i+1][j+1]:
                dp[i+1][j+1] = m
    return dp[n1][n2]
