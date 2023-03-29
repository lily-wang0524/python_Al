#快速排序

#插入p元素的核心函数
def partition(li,left,right): #li-列表，left和right表示列表范围
    tmp = li[left] #保存列表的第一个元素，即p元素
    while left < right: #当left指针在right指针的左侧时，循环继续
        while left < right and li[right] >= tmp: #从右往左找小于p元素的值
        #由于right往左移动会-1，若无法找到小于p元素的值，也需要确保跳出while循环，所以需要加left<right
            right -= 1 #right往左移一步
        li[left] = li[right] #从右往左找到小于p元素的值后，将其移动到左边空位上
        while left < right and li[left] <= tmp: #从左往右找，大于p元素的值，若小于p元素继续循环
        #与上一个while中的left<right相同，需要确保若无法找到大于p元素的值，也需要跳出循环；
        #且上一个while循环后已找到p元素的位置则不再进入该循环
            left += 1 #left往右移一步
        li[right] = li[left] #从左往右找到大于p元素的值，移到右侧空位上
    li[left] = tmp #当left=right时，p元素归位
    return left  #返回p元素的索引（位置）

# li = [5,7,4,6,9,8,3,0,1]
# partition(li,0,len(li)-1)
# print(li)


def quick_sort(li,left,right):
    if left < right: #确保列表元素大于2
        mid = partition(li,left,right) 
        quick_sort(li,left,mid-1) #p元素左侧范围left到mid-1
        quick_sort(li,mid+1,right) #p元素右侧范围mid+1到right

lis = [5,7,4,2,9,3,0,8]
quick_sort(lis,0,len(lis)-1)
print(lis)
    