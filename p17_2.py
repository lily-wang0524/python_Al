import random
from cal_time import cal_time
import copy #复制模块 
import sys

sys.setrecursionlimit(10000) #sys模块，修改最大递归深度

#冒泡排序
@cal_time
def bubble_sorted1(li):
    for i in range(len(li)-1): #排序将进行n-1趟，最后一个位置不需要再遍历
        exchange = False #判断跑完一趟是否有元素交换
        for j in range(len(li)-i-1):  #每趟的无序区间，只有无序区间需要排序
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j] #序列内部对调位置
                exchange = True
        # print(li)
        if not exchange: #如果未发生交换，跳出循环，输出结果
             return 

#快速排序
def partition(li,left,right): #li-列表，left和right表示列表范围
    tmp = li[left] #保存列表的第一个元素，即p元素
    while left < right: #当left指针在right指针的左侧时，循环继续
        while left < right and li[right] >= tmp: #从右往左找小于p元素的值
            right -= 1 #right往左移一步
        li[left] = li[right] #从右往左找到小于p元素的值后，将其移动到左边空位上
        while left < right and li[left] <= tmp: #从左往右找，大于p元素的值，若小于p元素继续循环
            left += 1 #left往右移一步
        li[right] = li[left] #从左往右找到大于p元素的值，移到右侧空位上
    li[left] = tmp #当left=right时，p元素归位
    return left  #返回p元素的索引（位置）

def _quick_sort(li,left,right):
    if left < right: #确保列表元素大于2
        mid = partition(li,left,right) 
        _quick_sort(li,left,mid-1) #p元素左侧范围left到mid-1
        _quick_sort(li,mid+1,right) #p元素右侧范围mid+1到right

#由于quick_sort()为递归，使用时间装饰器需要在外面加一个包装，否则每次递归都会调用时间装饰器
@cal_time
def quick_sort(li):
    _quick_sort(li,0,len(li)-1)

# li = list(range(10000)) #创建一个大规模列表
# random.shuffle(li) #打乱列表顺序

# li1 = copy.deepcopy(li) #深度复制li列表
# li2 = copy.deepcopy(li) #深度复制li列表，是li1与li2相同

# quick_sort(li1)
# bubble_sorted1(li2)

#大规模倒序，最坏情况示例
li = list(range(2500,0,-1)) #倒序排序
lis = list(range(2500)) #正序
random.shuffle(lis) #打乱排序
quick_sort(li)
quick_sort(lis)


