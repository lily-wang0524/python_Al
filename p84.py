# 数字拼接，得到最大整数

from functools import cmp_to_key # 排序模块
li = [32, 94, 128, 1286, 6, 71]

# 根据贪心算法，将数字字符串相连后更大的数字交换位置，后拼接。
# 降序排序，原理在知识点已解析
def xy_cmp(a,b):
    if a + b < b + a: # 交换位置
        return 1 
    else:
        return -1  # 不交换位置
    
def number_join(li): # 数字拼接
    li = list(map(str, li))  # 转换为字符串
    li.sort(key=cmp_to_key(xy_cmp))  # 按xy_cmp函数的排列要求排序
    return "".join(li)  # 拍好序后的列表拼接

print(number_join(li))