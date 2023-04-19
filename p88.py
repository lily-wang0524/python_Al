import time
# 递归求解斐波那契数列
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else: # n > 2
        res = fibnacci(n-1) + fibnacci(n-2) # 递推式
        return res

# t1 = time.time()   # 开始时间
# print(fibnacci(40)) # 运行程序
# t2 = time.time() # 结束时间
# print(f"递归运行时间：{t2-t1}") # 运行时间

# 非递归求解斐波那契数列
def fibnacci_no_rec(n):
    res = [0, 1, 1] # 结果列表，n=0，n=1，n=2时，结果已知
    if n > 2: 
        # 循环递推式，计算结果
        for i in range(n-2): # 例如n=3时，只需要循环一次
            num = res[-1] + res[-2] # 列表的最后一位和列表最后第二位，对应保存的n-1和n-2的值
            res.append(num) # 结果加入到列表中
    return res[n] # 列表第n项，不是res[-1],res有原始3个元素，n<=2时，res[-1]一直是1

t1 = time.time() # 开始时间
print(fibnacci_no_rec(40)) # 运行程序
t2 = time.time() # 结束时间
print(f"非递归运行时间：{t2-t1}")