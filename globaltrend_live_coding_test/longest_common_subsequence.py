def longest_common_subsequence(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    
    table = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    
    for i in range(1, l1+1):
        for j in range(1,l2+1):
            if string1[i-1] == string2[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    return table[l1][l2];
    
string1 = input("First String: ")
string2 = input("Second String: ")

print(longest_common_subsequence(string1, string2))
