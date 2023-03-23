# lis = [1,3,7,4,9,0]
# for i, val in enumerate(lis,1): #多用于在for循环中得到计数，利用它可以同时获得索引和值
#     print(f"index is {i}, the value is {val}")

# 顺序查找，时间复杂度O(n)
def linear_search(li,val):
    for ind, v in enumerate(li): #使用enumerate函数，输出索引和值
        if v == val:  #当当前值等于所需要的值
            return ind  #返回索引
    else:
        return None  #针对最后一个if的else，最后一个if仍旧不成立，则输出None
    
lis = [1,6,7,8,56,7,0,23,5]
lin = linear_search(lis,0)
print(lin)

#顺序查找——不用enumerate()函数
def lin_search(data, value):
    for i in range(len(data)):  #len()得到列表的长度，range()函数生成连续整数
        if data[i] == value:
            return i
    else:
        return None
    
li = lin_search(lis,0)
print(li)