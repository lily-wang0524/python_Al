# 钢条切割问题：自底向上——动态规划解法

import time

# 时间装饰器
def cal_time(func):
    def wrapper(*args, **kwargs): #函数参数不确定的时候，用*args和**kwargs，前者叫位置参数，后者叫关键字参数。
        t1 = time.time()
        result = func(*args, **kwargs) #运行被装饰的函数
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__,t2-t1)) #func.__name__装饰器的函数，表示函数名称
        return result
    
    return wrapper

# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30] # 钢条不同长度价格，其索引即为钢条长度
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]

@cal_time
def cut_rod_dp(p, n):
    r = [0] # n=0时，r为0
    for i in range(1, n+1): # 需要求解r1~rn，因此循环1~n
        res = 0  # ri的初始值为0
        for j in range(1, i+1): # n=i时，ri = max(p1+ri-1,...,pi+r0),每个ri循环j从1~i
            res = max(res, p[j] + r[i-j])  # 每个子问题求解
        r.append(res) # 每个ri存储到列表中方便取用
    return r[n]  

print(cut_rod_dp(p,20))


