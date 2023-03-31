#topk问题——堆排序实现
#堆排序是比较排序
#小根堆的向下调整
def sift(li,low,high): # 堆排序的向下调整
    i = low  # i是最开始指向堆顶位置,后面指向父节点
    j = 2 * i + 1 # j是i的左孩子
    tmp = li[low] # 把堆顶存起来
    while j <= high: # 只要j位置有元素，即i的左孩子索引不超过堆的最后一个元素
        # 结束该if，得到j指向两个孩子节点中值更小的节点。
        if j + 1 <= high and li[j] > li[j+1]: # 右孩子比左孩子小，且右孩子存在
            j = j + 1 # j指向右孩子
        if li[j] < tmp:  # 当前孩子节点的元素比取下来的值小
            li[i] = li[j]  # 将j指向的元素移到空位上，i位置因为取走了数，是空的状态。
            i = j  # 往下看一层，得到新的i
            j = 2 * i + 1  #得到新的j
        else: # tmp小于li[j],将tmp放在i的空位上
            li[i] = tmp #将tmp放在某一层的父节点位置
            break  # 结束while循环
    else: # j > high时，i指向的是叶子节点，其没有孩子节点，这是tmp直接放到i所在空位上
        li[i] = tmp

def topk(li, k): # topk问题
    heap = li[0:k] # 切片操作，包前不包后，实际取的索引0-(k-1)的k个数
    # 1、建小根堆
    for i in range((k-2)//2, -1, -1): # 从后往前，堆顶的下标是0，倒序。
        sift(heap, i, k-1) # 向下调整
    # 2、对比
    # 剩余从第k+1个数到最后一个数，即对应数的索引为从k到len(li)-1,range包前不包后，要写到len(li)
    for i in range(k, len(li)):
        if li[i] > heap[0]: # 列表值大于堆顶值
            heap[0] = li[i] # 覆盖原堆顶值
            sift(heap, 0, k-1) 
    #3、挨个出数-堆排序
    for i in range(k-1, 0, -1): # i指向当前堆的最后一个元素
        heap[i], heap[0] = heap[0], heap[i]  #不断用最后一个数替换堆顶
        sift(heap, 0, i-1) 

    return heap

lis = [5,3,4,7,2,8,9]
maxk = topk(lis,3)
print(maxk)

