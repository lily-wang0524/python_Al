from cal_time import cal_time

# 线性查找
@cal_time
def linear_search(li,val):
    for ind, v in enumerate(li): #使用enumerate函数，输出索引和值
        if v == val:  #当当前值等于所需要的值
            return ind  #返回索引
    else:
        return None

#二分查找  
@cal_time
def binary_search(li,val):
    left = 0
    right = len(li) - 1 
    while left <= right:
        mid = (left + right) // 2
        if  li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None
    
lis = list(range(10000000))
binary_search(lis,389000)
linear_search(lis,389000)


