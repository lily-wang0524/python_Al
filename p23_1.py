#堆排序
'''
description: 
param {*} li:列表
param {*} low:堆的根节点位置
param {*} high:堆的最后一个元素的位置
return {*}
'''
def sift(li,low,high): # 堆排序的向下调整
    i = low  # i是最开始指向堆顶位置,后面指向父节点
    j = 2 * i + 1 # j是i的左孩子
    tmp = li[low] # 把堆顶存起来
    while j <= high: # 只要j位置有元素，即i的左孩子索引不超过堆的最后一个元素
        # 结束该if，得到j指向两个孩子节点中值更大的节点。
        if j + 1 <= high and li[j] < li[j+1]: # 右孩子比左孩子大，且右孩子存在
            j = j + 1 # j指向右孩子
        if li[j] > tmp:  # 当前孩子节点的元素比取下来的值大
            li[i] = li[j]  # 将j指向的元素移到空位上，i位置因为取走了数，是空的状态。
            i = j  # 往下看一层，得到新的i
            j = 2 * i + 1  #得到新的j
        else: # tmp大于li[j],将tmp放在i的空位上
            li[i] = tmp #将tmp放在某一层的父节点位置
            break  # 结束while循环
    else: # j > high时，i指向的是叶子节点，其没有孩子节点，这是tmp直接放到i所在空位上
        li[i] = tmp

# 堆排序主体
def heap_sort(li): # 堆排序，参数为列表
    n = len(li) # 列表长度
    for i in range((n-2)//2, -1, -1): # 从后往前，堆顶的下标是0，range()函数包前不包后，需写到-1，-1为步长，倒序。
        # i表示建堆时，需要调整的根节点
        #开始做堆的向下调整
        sift(li,i,n-1) #i为堆顶low，n-1为树的最后一个元素high，不用寻找每个子树的最后一个元素，也可确保j不越界
    #完成上面的for循环，建堆完成
    #下面开始挨个出数
    for i in range(n-1, 0, -1):  #range()用-1做倒序，列表的最后剩下的数不需要排序，不需要取到索引0
        # i指向当前堆的最后一个元素，不断往前推进。
        #互换堆顶元堆的最后一个元素,堆顶元素填到列表后面
        li[i], li[0] = li[0], li[i]  # 无序区为除了根节点其他子树为堆的二叉树
        sift(li, 0, i-1) # i-1是新的high，向下调节无序区，成为堆;
    print(li)

li = [4,6,2,8,7,5,0,9]
heap_sort(li)