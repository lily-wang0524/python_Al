# 分数背包-贪心算法
# 问题：
# 商品1：v1=60 ，w1=10
# 商品2∶v2=100 ，w2=20
# 商品3∶v3=120， w3=30
# 背包容量:W=50

goods = [(60,10),(120,30),(100,20)] # 每个元组代表（价值，重量），也可以用字典表示
goods.sort(key= lambda x : x[0] / x[1], reverse= True) # 根据商品单价降序排序
print(goods) 

def fractional_backpack(goods, w): # goods是列表降序排序后，w表示背包容量
    m = [0 for i in range(len(goods))] # 表示各商品可装的数量
    total_v = 0 # 总价值
    # 循环-根据贪心算法原则，求解
    for i, (price, weight) in enumerate(goods):
        if w >= weight: # 背包空间可以带走整个商品
            m[i] = 1  # 商品整个带走
            w = w - weight # 剩余背包容量
            total_v += price # 商品价值相加
        else: # w<weight, 无法将整个商品带走，只能装下一部分
            m[i] = w / weight # 可带走部分
            w = 0 # 背包容量用完
            total_v += price * m[i]  # 商品总价值 * 带走的商品数量
            break  # 跳出循环
    return total_v, m 

print(fractional_backpack(goods, 50))