""" Longest Common Sequence
    return LCS's length, all LCSs
    S, T の LCS の長さと 全ての LCS を求めて返す """
    
def LCS(S, T):
    lenS, lenT = len(S), len(T)
    lcs_set = [[[] for j in range(lenT + 1)] for i in range(lenS + 1)]
    for i in range(0, lenS + 1):
        lcs_set[i][0].append("")
    for j in range(1, lenT + 1):
        lcs_set[0][j].append("")
    for i in range(1, lenS + 1):
        for j in range(1, lenT + 1):
            if S[i-1] == T[j-1]:
                for x in lcs_set[i-1][j-1]:
                    lcs_set[i][j].append(x + S[i-1])
            else:
                if len(lcs_set[i-1][j][0]) < len(lcs_set[i][j-1][0]):
                    lcs_set[i][j] = lcs_set[i][j-1]
                elif len(lcs_set[i-1][j][0]) > len(lcs_set[i][j-1][0]):
                    lcs_set[i][j] = lcs_set[i-1][j]
                else:
                    lcs_set[i][j] = lcs_set[i-1][j] + lcs_set[i][j-1]
            lcs_set[i][j] = list(set(lcs_set[i][j]))
    return lcs_set[lenS][lenT]
