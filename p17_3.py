#最坏情况修正
import random
from cal_time import cal_time
import copy #复制模块 
import sys

sys.setrecursionlimit(10000) #sys模块，修改最大递归深度

#快速排序
def partition(li,left,right): #li-列表，left和right表示列表范围
    num = random.randint(left,right) #生成一个随机整数
    li[left],li[num] = li[num],li[left] #交换无序区第一个数值，更改为随机获取的数，以打乱列表现有顺序
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

li = list(range(2500,0,-1))
quick_sort(li)