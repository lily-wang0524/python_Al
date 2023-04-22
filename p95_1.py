# 欧几里得算法——最大公约数

def gcd_1(a,b): # 最大公约数-递归，a，b是两个数值
    if b == 0: # 递归终止条件
        return a
    else:
        return gcd_1(b, a % b) # 公式gcd(a,b) = gcd(b, a mod b)

print(gcd_1(12,16))

def gcd_2(a, b): # 最大公约数-非递归，a，b是两个数值
    while b > 0: # b = 0时就得的a就是最后求的值
        r = a % b # 循环中a，b值一直在变化，需要先存储在一个变量中，不能直接用a%b
        a = b
        b = r
    return a

print(gcd_2(12,16))