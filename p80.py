# 找零问题

t = [100,50,20,5,1] # 手上的钱,倒序排列

def change(t, n): # n是找零的钱数
    m = [0 for _ in range(len(t))] # 找零张数
    for i,money in enumerate(t):  # i是列表索引，money是索引对应的值
        m[i] = n // money   # m列表的第i个值，是找零的钱除以钱币的面值
        n = n % money # 剩余需找零的钱是取余
    return m,n # 找零张数列表，以及找不开的张数

print(change(t, 376))