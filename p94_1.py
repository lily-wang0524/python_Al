# 最长公共子序列求解

def lcs_length(x,y): # 公共子序列长度，x，y: 字符串、列表等序列
    m = len(x) # x序列长度
    n = len(y) # y序列长度
    c = [[0 for i in range(n + 1)] for _ in range(m+1)] # 创建m行n列二维数组，初始值为0 
    for i in range(1, m+1):  # 按数组的行求，x0都为0不用求，所以从1开始
        for j in range(1, n+1): # 数组每行中的遍历，y0都为0，不用求
            if x[i - 1] == y[j - 1]:  # x[i-1]其实是字符串的i，因为i=0在二维列表中都是0，不求解，但是在字符串中仍需要从索引0遍历
                c[i][j] = c[i-1][j-1] + 1 # 递推式
            else:  # xi！=yi
                c[i][j] = max(c[i-1][j],c[i][j-1])  # 递推式
    
    return c[m][n]    # x和y的最后一个元素对比完，二维数组的最后一位

print(lcs_length('ABCBDAB', 'BDCABA'))
