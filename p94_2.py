# 最长公共子序列求解序列值

# 动态规划求解，存储解及解的计算过程
def lcs(x,y): # 求解并存储箭头方向，x，y为字符串、列表等序列
    m = len(x) # x的长度
    n = len(y) # y的长度
    c = [[0 for i in range(n+1)] for _ in range(m+1)] # 二维数组，初始值为0，用于存储长度结果
    d = [[0 for i in range(n+1)] for _ in range(m+1)] # 二维数组，初始值为0，用于存储箭头方向,1表示左上，2表示上，3表示左
    for i in range(1,m+1): # 按行遍历二维数组
        for j in range(1,n+1): # 每行的各数值遍历， c0j和ci0相关的值都为0，所以均从1开始
            if x[i - 1] == y[j - 1]: # xi=yi的情况，二维数组中i，j=0时，都为0已经确定，但字符串x，y仍需从0开始遍历
                c[i][j] = c[i - 1][j - 1] + 1 # 递推式
                d[i][j] = 1 # 箭头方向左上方
            elif c[i][j - 1] > c[i - 1][j]: # 递推式，选择更大的
                c[i][j] = c[i][j - 1]
                d[i][j] = 3 # 箭头左边
            else: # c[i-1][j] >= c[i][j-1]
                c[i][j] = c[i - 1][j]
                d[i][j] = 2 # 箭头上方
    return c[m][n], d

# 回溯算法
def lcs_trackback(x,y): # 最长公共子序列的序列
    c, d = lcs(x, y) # c长度，d箭头方向
    i = len(x) # x的长度
    j = len(y) # y的长度
    res = [] # 结果列表
    while i > 0 and j > 0 : # 序列x和y还有值未比对，任何一个序列为0了都不再继续
        if d[i][j] == 1: # 箭头左上方 ——> 匹配
            res.append(x[i - 1])  # 二维列表中i=0时，值为0，但是序列x的值是从0开始遍历的
            i = i - 1 # 位置移到左上位置
            j = j - 1
        elif d[i][j] == 2: # 箭头上方->不匹配
            i = i - 1 # 位置往上移一格
        else: # dij = 3 ，箭头左向
            j = j - 1 # 位置往左移一格
    
    return "".join(reversed(res))  # 列表翻转，并将列表用''连接成字符串

print(lcs_trackback("ABCBDAB", "BDCABA"))
