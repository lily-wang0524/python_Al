# topk问题——冒泡排序
'''
description: 
param {*} li:列表
param {*} k:取最大前k个数
return {*}
'''
def topk_bubble1(li, k):  #创建空列表存数
    result = [] 
    for i in range(k): # 第i趟，完全的冒泡排序一共n-1趟，只取前k个数，经过k趟
        for j in range(len(li)-i-1): #range内为无序区范围,j指针不指向最后一个元素
            if li[j] > li[j+1]:  # 前一个数大于后一个数
                li[j+1], li[j] = li[j], li[j+1] #交换两个数的位置
        result.append(li[len(li)-i-1]) # 取第i趟获得的最大数，即该趟无序区排序后得到的最后一个元素
    return result
    
#在排序中切片
def topk_bubble2(li, k):
    n = len(li) # 列表长度
    for i in range(k):
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    result = li[(n-k):n] #切片，切片包前不包后
    return result

def topk_bubble3(li, k):
    n = len(li) # 列表长度
    for i in range(k):
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
        print(li[n-i-1], end = " ")  #打印每次无序区排序的最后一个元素，即冒出来的数


lis = [1,4,5,3,6,2]
res1 = topk_bubble1(lis,2)
res2 = topk_bubble2(lis,2)

print(res1)
print(res2)
topk_bubble3(lis,2)