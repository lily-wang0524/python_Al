# 钢条切割问题：重构解

# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30] # 钢条不同长度价格，其索引即为钢条长度
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]

def cut_rod_extend(p,n): # 求解ri，si
    r = [0] # ri列表，i=0时，价值为0
    s = [0]  # si列表，i=0时，左侧切割长度为0
    for i in range(1,n+1): # 求解r1~rn的n个解
        res_r = 0  # ri的值，表示最大收益
        res_s = 0  # si的值，价格最大值对应方案左边不切割的长度
        for j in range(1,i+1):  #长度为i的最高价值ri = max(p1+ri-1,...,pi+r0),所以对比1~i个解的大小
            if p[j] + r[i-j] > res_r:  # 对比大小
                res_r = p[j] + r[i-j]
                res_s = j  # 对应的p[j]，即左边长度
        r.append(res_r) # ri结果存储至列表
        s.append(res_s) # si结果存储至列表

    return r[n],s # rn的最大价值，s是左边不在切割的长度列表

def cut_rod_solution(p,n): # 求解具体切割方案
    r, s = cut_rod_extend(p,n) # 得到r，s列表
    ans = [] # 切割方案列表
    while n > 0: # 当钢条还有长度时，循环
        ans.append(s[n]) # 将n最大收益时左边不切割的长度存储到方案列表
        n -= s[n] # 钢条右边可继续切割的长度为n-sn
    return ans


r,s = cut_rod_extend(p, 15)    # 最大收益值，及最大收益时左边不再切割部分长度列表
ans = cut_rod_solution(p, 15) # 最优切割方案
print(s)
print(r)
print(ans)