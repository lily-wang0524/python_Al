#冒泡排序
# def bubble_sorted(li):
#     for i in range(len(li)-1): #排序将进行n-1趟，最后一个位置不需要再遍历
#         for j in range(len(li)-i-1):  #每趟的无序区间，只有无序区间需要排序
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j] #序列内部对调位置
#             # print(li)

# lis = [3,5,1,2,9]
# bubble_sorted(lis)
# print(lis)

#优化后的冒泡排序，减少空跑
def bubble_sorted1(li):
    for i in range(len(li)-1): #排序将进行n-1趟，最后一个位置不需要再遍历
        exchange = False #判断跑完一趟是否有元素交换
        for j in range(len(li)-i-1):  #每趟的无序区间，只有无序区间需要排序
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j] #序列内部对调位置
                exchange = True
        print(li)
        if not exchange: #如果未发生交换，跳出循环，输出结果
             return 

lis = [3,5,1,2,9]
bubble_sorted1(lis)
