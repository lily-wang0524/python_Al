# 钢条切割问题：自顶向下——递归解法

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

# 未简化前递推式
def cut_rod_recurision_1(p, n):
    # 长度为0，钢条无价值
    if n == 0:
        return 0
    # 递归实现递推式
    else: 
        res = p[n] # 不切割，全局变量
        for i in range(1,n): # 递归的结束条件，循环次数为r1~rn-1
            # 递推式，递归的是不同的切割方法
            res = max(res,cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n-i)) 
        return res

@cal_time
def c1(p,n): # 递归用语法糖会每层都运行，所以加个外壳
    return cut_rod_recurision_1(p,n)

print(c1(p,15))

# 简化后递推式
def cut_rod_recurision_2(p, n): # p是钢条不切割价格，n钢条长度
    # 长度为0，钢条无价值
    if n == 0:
        return 0
    # 简化后递推式
    else:
        res = 0 # 初始结果为0
        for i in range(1,n+1): # 从p1+rn-1到pn+r0，因此循环1~n。
            res = max(res, p[i] + cut_rod_recurision_2(p, n-i))  # 递推式
        return res

@ cal_time   
def c2(p, n):
    return cut_rod_recurision_2(p, n)
    
print(c2(p,15))